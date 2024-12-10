from bd.bd_sinc_alch import engin
from sqlalchemy import text

with engin.connect() as conn:
    res = conn.execute(text('SELECT VERSION()'))
    print(f'{res.all()}')