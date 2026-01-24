from app.services.system_service import SystemService

def test_health():
    service=SystemService()
    result=service.health()
    assert result.status=="ok"