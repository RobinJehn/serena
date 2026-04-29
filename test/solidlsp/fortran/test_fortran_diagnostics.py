import pytest

from solidlsp import SolidLanguageServer
from solidlsp.ls_config import Language
from test.solidlsp.util.diagnostics import assert_file_diagnostics


@pytest.mark.fortran
@pytest.mark.xfail(reason="fortls 3.2.2 does not implement textDocument/diagnostic or publish diagnostics for opened files")
class TestFortranDiagnostics:
    @pytest.mark.parametrize("language_server", [Language.FORTRAN], indirect=True)
    def test_file_diagnostics(self, language_server: SolidLanguageServer) -> None:
        assert_file_diagnostics(
            language_server,
            "diagnostics_sample.f90",
            (),
            min_count=1,
        )
