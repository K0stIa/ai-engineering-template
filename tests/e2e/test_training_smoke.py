"""Opt-in synthetic PyTorch overfit check; not real-model acceptance evidence."""

import pytest


@pytest.mark.gpu
@pytest.mark.integration
def test_tiny_batch_overfits():
    import torch

    if not torch.cuda.is_available():
        pytest.fail("GPU tier selected but CUDA is unavailable; this is not a passing skip.")
    torch.manual_seed(7)
    x = torch.randn(16, 4, device="cuda")
    target = x.sum(dim=1, keepdim=True)
    model = torch.nn.Linear(4, 1).cuda()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
    first_loss = torch.nn.functional.mse_loss(model(x), target).item()
    for _ in range(100):
        optimizer.zero_grad()
        loss = torch.nn.functional.mse_loss(model(x), target)
        assert torch.isfinite(loss).item()
        loss.backward()
        optimizer.step()
    assert torch.nn.functional.mse_loss(model(x), target).item() < first_loss * 0.01
