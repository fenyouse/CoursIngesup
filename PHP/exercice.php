<?php
class enfant{
	private $_nom;
	private $_prenom;
	private $_age;




     public function __construct() {   
				   $a = func_get_args();   
				    $i = func_num_args();   
				     $fct ='__construct'.$i;  
				      if (method_exists($this,$fct)) {    
				      	 call_user_func_array(array($this,$fct),$a);} }

		private function __construct1 ($a1)  {echo $a1.',';}

		private function __construct2 ($a1, $a2) {echo $a1.',';}

		private function __construct3 ($a1, $a2, $a3) {echo $a1;}

	



	}



$moi =new enfant('toto');
$toi =new enfant('riri');
$lui =new enfant('loulou');




	 ?>