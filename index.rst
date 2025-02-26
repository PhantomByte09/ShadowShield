Welcome to ShadowShield's documentation!
========================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Introduction
------------
ShadowShield هي أداة متقدمة لحماية الخصوصية والأمان السيبراني، توفر ميزات مثل:
- تغيير MAC و IP لإخفاء الهوية.
- جدار ناري ونظام كشف الاختراقات (IDS).
- تشفير AES-256 للملفات والاتصالات.

Installation
------------
لتثبيت الأداة:
```bash
pip install -r requirements.txt
python setup.py install
```

Usage
-----
لتشغيل الأداة:
```bash
python main.py
```

Modules
-------
- anonymizer.py: تغيير MAC و IP.
- encryption.py: تشفير البيانات.
- firewall.py: تشغيل الجدار الناري.
