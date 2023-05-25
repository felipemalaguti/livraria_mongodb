import psycopg2


class ConexaoFactory:

    def get_conexao(self):
        return psycopg2.connect(host='silly.db.elephantsql.com', database='ntbnfdrz' , user='ntbnfdrz' , password='XxBeTZSKnOEPwHbG1tkQf8ZrsVw0LtAF' )

