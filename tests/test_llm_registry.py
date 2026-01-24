import pytest
from app.infra.llm.registry import REGISTRY
from app.infra.llm.dummy import DummyLLM
from app.infra.llm.factory import get_llm
from app.core.exceptions import AppException


def test_llm_registry_valid_provider():
    llm=get_llm("dummy")
    assert isinstance(llm,DummyLLM)

def test_get_llm_invalid_provider():
    with pytest.raises(AppException):
        get_llm("invalid_provider")

def test_different_instance():
    llm1=get_llm("dummy")
    llm2=get_llm("dummy")

    assert llm1 is not  llm2
