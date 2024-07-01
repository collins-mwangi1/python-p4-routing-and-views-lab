import io
import sys
from server.app import app

class TestApp:
    '''Flask application test cases.'''

    def test_index_route(self):
        '''Test if "/" returns status code 200.'''
        client = app.test_client()
        response = client.get('/')
        assert response.status_code == 200

    def test_index_text(self):
        '''Test if "/" displays expected h1 content.'''
        client = app.test_client()
        response = client.get('/')
        assert '<h1>Python Operations with Flask Routing and Views</h1>' in response.data.decode()

    def test_print_route(self):
        '''Test if "/print/hello" returns status code 200.'''
        client = app.test_client()
        response = client.get('/print/hello')
        assert response.status_code == 200

    def test_print_text(self):
        '''Test if "/print/hello" displays "hello".'''
        client = app.test_client()
        response = client.get('/print/hello')
        assert response.data.decode() == 'hello'

    def test_print_to_console_route(self):
        '''Test printing text to console from "/print_to_console/hello".'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        
        with app.test_client() as client:
            client.get('/print_to_console/hello')
            
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue().strip() == 'hello'

if __name__ == '__main__':
    test_app = TestApp()
    test_app.test_index_route()
    test_app.test_index_text()
    test_app.test_print_route()
    test_app.test_print_text()
    test_app.test_print_to_console_route()
