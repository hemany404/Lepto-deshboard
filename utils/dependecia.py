def limpar_e_converter(col):
        return (
            col.astype(str).str.replace('%', '', regex=False).str.replace(',', '.', regex=False).str.replace(r'[^\d\.\-]', '', regex=True).replace('', '0').astype(float)
        )