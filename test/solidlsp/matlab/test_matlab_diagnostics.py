import pytest

from solidlsp import SolidLanguageServer
from solidlsp.ls_config import Language
from test.solidlsp.util.diagnostics import assert_file_diagnostics


@pytest.mark.matlab
class TestMatlabDiagnostics:
    @pytest.mark.parametrize("language_server", [Language.MATLAB], indirect=True)
    def test_file_diagnostics(self, language_server: SolidLanguageServer) -> None:
        assert_file_diagnostics(
            language_server,
            "diagnostics_sample.m",
            (),
            min_count=1,
        )
