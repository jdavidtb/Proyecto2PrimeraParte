import unittest
from datetime import datetime
from model.factura import Factura

class TestFactura(unittest.TestCase):

    def setUp(self):
        self.factura = Factura("F12345")

    def test_inicializacion_factura(self):
        self.assertEqual(self.factura.IDfactura, "F12345")
        self.assertIsInstance(self.factura.fecha, datetime)
        self.assertEqual(self.factura.valor_total, 0.0)
        self.assertIsNone(self.factura.cedula)
        self.assertEqual(len(self.factura.pedidos), 0)

    def test_modificar_IDfactura(self):
        self.factura.IDfactura = "F67890"
        self.assertEqual(self.factura.IDfactura, "F67890")

    def test_modificar_fecha(self):
        nueva_fecha = datetime(2022, 10, 17)
        self.factura.fecha = nueva_fecha
        self.assertEqual(self.factura.fecha, nueva_fecha)

    def test_fecha_no_datetime(self):
        with self.assertRaises(ValueError):
            self.factura.fecha = "2022-10-17"

    def test_valor_total_negativo(self):
        with self.assertRaises(ValueError):
            self.factura.valor_total = -100.0

    def test_agregar_pedido(self):
        pedido_mock = "pedido_mock"
        self.factura.agregar_pedido(pedido_mock)
        self.assertEqual(len(self.factura.pedidos), 1)
        self.assertEqual(self.factura.pedidos[0], pedido_mock)

if __name__ == "__main__":
    unittest.main()
