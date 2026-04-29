import pytest

from solidlsp import SolidLanguageServer
from solidlsp.ls_config import Language
from test.solidlsp.util.diagnostics import assert_file_diagnostics


@pytest.mark.solidity
class TestSolidityDiagnostics:
    @pytest.mark.parametrize("language_server", [Language.SOLIDITY], indirect=True)
    def test_file_diagnostics(self, language_server: SolidLanguageServer) -> None:
        assert_file_diagnostics(
            language_server,
            "contracts/DiagnosticsSample.sol",
            (),
            min_count=1,
        )
