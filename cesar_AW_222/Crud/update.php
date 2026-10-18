<?php 
    include("conexion.php");
    $con = conectar();

    $id = $_GET['id'];

    $sql = "SELECT * FROM alumnos WHERE matricula='$id'";
    $query = mysqli_query($con, $sql);
    $row = mysqli_fetch_array($query);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Editar Alumno</title>
</head>
<body>
    <div>
        <h1>Editar Información del Alumno</h1>
      
        <form action="editar.php" method="POST">
            

            <input type="hidden" name="matricula" value="<?php echo $row['matricula']; ?>">
            
            <div style="display: flex; flex-direction: column; gap: 10px; width: 300px;">
                <label>Nombre:</label>
                <input type="text" name="nombre" value="<?php echo $row['nombre']; ?>">
                
                <label>Apellido Paterno:</label>
                <input type="text" name="apellido_p" value="<?php echo $row['apellido_p']; ?>">
                
                <label>Apellido Materno:</label>
                <input type="text" name="apellido_m" value="<?php echo $row['apellido_m']; ?>">
                
                <label>Edad:</label>
                <input type="text" name="edad" value="<?php echo $row['edad']; ?>">
                
                <button type="submit">Actualizar Datos</button>
            </div>
        </form>
    </div>
</body>
</html