git clone [<repo>](https://github.com/JuniorNS96/siteEshop.git)
cd projeto

python -m venv venv
source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload