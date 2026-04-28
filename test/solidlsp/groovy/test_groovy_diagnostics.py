import pytest

from solidlsp import SolidLanguageServer
from solidlsp.ls_config import Language
from test.solidlsp.util.diagnostics import assert_file_diagnostics


@pytest.mark.groovy
class TestGroovyDiagnostics:
    @pytest.mark.parametrize("language_server", [Language.GROOVY], indirect=True)
    def test_file_diagnostics(self, language_server: SolidLanguageServer) -> None:
        assert_file_diagnostics(
            language_server,
            "src/main/groovy/com/example/DiagnosticsSample.groovy",
            (),
            min_count=1,
        )
