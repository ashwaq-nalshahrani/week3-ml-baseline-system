from .cli import app


def main():
    """
    نقطة الدخول الرئيسية للتطبيق.
    تقوم باستدعاء تطبيق Typer المعرف في ملف cli.py
    """
    app()


if __name__ == "__main__":
    main()
