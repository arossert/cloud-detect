import pytest   # noqa: F401

from cloud_detect.providers import AzureProvider


def test_reading_correct_vendor_file():
    provider = AzureProvider()
    assert provider.check_vendor_file('tests/provider_files/azure') is True


def test_reading_invalid_vendor_file():
    provider = AzureProvider()
    assert provider.check_vendor_file('tests/provider_files/aws') is False
    assert provider.check_vendor_file('') is False


@pytest.mark.asyncio
async def test_invalid_metadata_server_check(aresponses):
    mock_host = 'testing_metadata_url.com'
    aresponses.add(
        mock_host, '/', 'GET', response={},
    )

    provider = AzureProvider()
    provider.metadata_url = f'https://{mock_host}'
    assert await provider.check_metadata_server() is True
