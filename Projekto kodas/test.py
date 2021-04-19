import unittest
import run

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = run.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        data = """<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Grįžtamojo ryšio sistema</title>
     <link rel="stylesheet" href="/static/css/bootstrap.css"> 
	 
	</head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-light bg-light" >
  <div class="container" height="200">
    <div class="navbar-header">
		  

		  
    </div>
    <div class="collapse navbar-collapse" id="navbarNav">
        
          <div class="my-2 my-md-0 mr-md-3">
            <a href="/"><img src="/static/imgs/home.png" alt="Pagrindinis" width="70" height="80"></a>
          </div>
			  
    </div>
    <div id="navbar" class="my-2 my-md-0 mr-md-3">
      
        <a class="btn btn-primary" href="/register"><h3>Registruotis</h3></a>
        <a class="btn btn-outline-primary" href="/login"><h3>Prisijungti</h3></a>
      
    </div><!--/.nav-collapse -->
  </div>
</nav>
    <br>
    <div class="container">
      
  





      
    <div class="jumbotron">
      <h1 class="display-4" align="center">TAPK MŪSŲ DALIMI,</h1>
      <p class="lead" align="center">kad geriau suvoktum save ir savo kompaniją!</p>
      <hr class="my-4">
      
      <h1 align="center"> <a href="/register" class="btn btn-primary btn-lg" >UŽSIREGISTRUOK JAU DABAR</a></h1>
	    <h5 align="center"><a href="/login"> <font color="#000000" ><b><u>Jau esi prisiregistravęs?</b></u></font></a></h5>
      
    </div>

    </div>


    
    <script src="/static/js/bootstrap.js"></script>
    <script src="//cdn.ckeditor.com/4.6.2/basic/ckeditor.js"></script>
	
    <script type="text/javascript">
      CKEDITOR.replace('editor')
    </script>
  </body>
  

<!-- Footer -->
<br>
<footer class="page-footer py-4 bg-dark text-white-50" >
    <!-- Footer Text -->
    <div class="container-fluid text-center text-md-left">
      <!-- Grid row -->
      <div class="row">
        <hr class="clearfix w-100 d-md-none pb-3">
        <!-- Grid column -->
        <div class="col-md-6 mt-md-0 mt-3">
          <!-- Content -->
          <h5 class="text-uppercase font-weight-bold">SUSISIEK SU MUMIS!</h5>
          <p>El. paštas: <a href="mailto: email@address.com">email@address.com</a> <br>
        </div>
        <!-- Grid column -->
        <!-- Grid column -->
        <div class="col-md-6 mb-md-0 mb-3">
          <!-- Content -->
          <h5 class="text-uppercase font-weight-bold">APSAUGA</h5>
          Visos teisės saugomos.</p>
        </div>
        <!-- Grid column -->
      </div>
      <!-- Grid row -->
    </div>
    <!-- Footer Text -->
    <!-- Copyright -->
    <div class="footer-copyright text-center py-3">© 2019 Copyright:
      <a href="https://www.company-name.com"> <font color="#606060">2019 COMPANY NAME Inc.</font></a>
    </div>
    <!-- Copyright -->
  </footer>
<!-- Footer -->


</html>"""
        data = data.encode()
        assert data in rv.data



if  __name__ == '__main__':
    unittest.main()
