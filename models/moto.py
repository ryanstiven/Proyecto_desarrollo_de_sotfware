from database import mysql

class Moto:

    @staticmethod
    def get_all():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM Moto")
        data = cursor.fetchall()
        cursor.close()
        return data

    @staticmethod
    def get_by_id(id):
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM Moto WHERE id_moto = %s", (id,))
        data = cursor.fetchone()
        cursor.close()
        return data

    @staticmethod
    def create(marca, modelo, cilindraje, anio, precio, id_proveedor):
        cursor = mysql.connection.cursor()
        cursor.execute("""
            INSERT INTO Moto (marca, modelo, cilindraje, anio, precio, id_proveedor)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (marca, modelo, cilindraje, anio, precio, id_proveedor))
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def update(id, marca, modelo, cilindraje, anio, precio, id_proveedor):
        cursor = mysql.connection.cursor()
        cursor.execute("""
            UPDATE Moto 
            SET marca=%s, modelo=%s, cilindraje=%s, anio=%s, precio=%s, id_proveedor=%s
            WHERE id_moto=%s
        """, (marca, modelo, cilindraje, anio, precio, id_proveedor, id))
        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def delete(id):
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM Moto WHERE id_moto=%s", (id,))
        mysql.connection.commit()
        cursor.close()