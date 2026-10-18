<?php
include("conexion.php");
$con = conectar();
//RECIBIMOS LA MATRICULA ENVIADA POR LA url
$matricula = $_GET['id'];

//Eliminamos al alumno de la tabla

$sql = "DELETE FROM alumnos WHERE matricula='$matricula'";

$query = mysqli_query($con, $sql);

//Verificamos si la consulta se ejecuto correctamente

if ($query){
    header("Location: alumnos.php");

}else{
    echo"Error al eliminar el alumno:" . mysqli_error("$con");
}
?>