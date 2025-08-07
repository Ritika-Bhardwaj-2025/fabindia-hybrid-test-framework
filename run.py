import os
import time
import datetime
import ssl
import base64
import subprocess
import sendgrid
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition


class BeautifulReporter:
    BASE_DIRECTORY = 'C:/Users/10835846/PycharmProjects/ProjectGladiator/Report'
    REPORT_DIRECTORY = os.path.join(BASE_DIRECTORY, "BeautifulReports")

    def __init__(self):
        os.makedirs(self.REPORT_DIRECTORY, exist_ok=True)

    def generate_report(self):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
        timestamped_folder = os.path.join(self.REPORT_DIRECTORY, f"BeautifulReports_{timestamp}")
        os.makedirs(timestamped_folder, exist_ok=True)

        report_path = os.path.join(timestamped_folder, "Report_Hybrid.html")

        try:
            # Run pytest and wait for it to complete
            subprocess.run([
                "pytest", "base.py",
                f"--html={report_path}",
                "--self-contained-html"
            ], check=True)
        except subprocess.CalledProcessError as e:
            print(" Some tests failed. Proceeding to send the report anyway.")
            # Optionally log or handle the error if needed

        # Ensure file is fully written
        time.sleep(2)

        if os.path.exists(report_path):
            self.send_report_via_sendgrid(report_path)
        else:
            print(" Report file was not generated.")

    def send_report_via_sendgrid(self, report_path):
        SENDGRID_API_KEY = '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'
        SENDER_EMAIL = 'aw9016226@gmail.com'
        RECIPIENT_EMAIL = 'valorantmorgan5@gmail.com'

        ssl._create_default_https_context = ssl._create_unverified_context

        sg = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)
        with open(report_path, 'rb') as f:
            data = f.read()
            encoded = base64.b64encode(data).decode()

        attachment = Attachment(
            FileContent(encoded),
            FileName(os.path.basename(report_path)),
            FileType("text/html"),
            Disposition("attachment")
        )

        mail = Mail(
            from_email=SENDER_EMAIL,
            to_emails=RECIPIENT_EMAIL,
            subject="Automation Test Report",
            plain_text_content="Please find the attached automation test report.",
        )
        mail.attachment = attachment

        try:
            response = sg.send(mail)
            print(f" Report sent successfully!")
            print(f"Status Code: {response.status_code}")
        except Exception as e:
            print(f"Failed to send email: {e}")


if __name__ == "__main__":
    reporter = BeautifulReporter()
    reporter.generate_report()
