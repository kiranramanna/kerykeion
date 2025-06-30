from pathlib import Path
from kerykeion import AstrologicalSubject, KerykeionChartSVG

class TestVedicChart:
    WRITE_TO_FILE = False
    SVG_DIR = Path(__file__).parent / 'svg'

    def setup_class(self):
        self.subject = AstrologicalSubject("Test Subject", 1990, 1, 1, 12, 0, "New York", "US")

    def test_vedic_chart_generation(self):
        """Tests the generation of the Vedic chart."""
        chart = KerykeionChartSVG(self.subject, chart_type="Vedic")
        svg_content = chart.makeTemplate()

        assert svg_content is not None
        assert "<svg" in svg_content
        assert "id='vedic_chart_grid'" in svg_content

        if self.WRITE_TO_FILE:
            output_path = self.SVG_DIR / "vedic_chart_test.svg"
            with open(output_path, "w") as f:
                f.write(svg_content)
