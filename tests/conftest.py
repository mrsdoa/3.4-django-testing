import pytest

pytest_plugins = [
    'tests.fixtures_api',
    'tests.fixtures_course_fabric',
    'tests.fixtures_student_fabric'
]

def pytest_addoption(parser):
    parser.addoption("--PALLADIUM_CONFIG", action="store")

@pytest.fixture
def PALLADIUM_CONFIG(request):
    return request.config.getoption("--PALLADIUM_CONFIG")