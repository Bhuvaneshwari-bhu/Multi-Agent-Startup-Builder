import json

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)

from config.settings import PDF_OUTPUT_PATH


def format_report(data):
    """
    Convert dictionaries and lists into readable text.
    """

    if isinstance(data, dict):

        lines = []

        for key, value in data.items():

            label = key.replace("_", " ").title()

            lines.append(f"<b>{label}:</b> {value}")

        return "<br/>".join(lines)

    if isinstance(data, list):

        return "<br/>".join(
            f"• {item}" for item in data
        )

    if data is None:
        return "N/A"

    return str(data).replace("\n", "<br/>")


def generate_pdf(state):

    pdf = SimpleDocTemplate(PDF_OUTPUT_PATH)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph("AI Startup Blueprint", styles["Title"])
    )

    content.append(Spacer(1, 18))

    sections = [
        ("Business", state.get("business_report")),
        ("Competitors", state.get("competitor_report")),
        ("Market", state.get("market_report")),
        ("Finance", state.get("finance_report")),
        ("SWOT", state.get("swot_report")),
        ("Pitch", state.get("pitch_report")),
        ("Roadmap", state.get("roadmap_report")),
    ]

    for title, report in sections:

        content.append(
            Paragraph(title, styles["Heading2"])
        )

        content.append(
            Paragraph(
                format_report(report),
                styles["BodyText"],
            )
        )

        content.append(
            Spacer(1, 12)
        )

    pdf.build(content)