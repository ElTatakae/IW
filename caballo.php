<?php

// Define el tamaño del tablero
$n = 8;

// Inicializa el tablero vacío
$tablero = array();
for ($i = 0; $i < $n; $i++) {
    $tablero[$i] = array();
    for ($j = 0; $j < $n; $j++) {
        $tablero[$i][$j] = 0;
    }
}

// Define la posición inicial del caballo en la esquina superior izquierda
$x = 0;
$y = 0;
$movimiento = 1;
$tablero[$x][$y] = $movimiento;

// Define los movimientos del caballo
$movimientos_x = array(2, 1, -1, -2, -2, -1, 1, 2);
$movimientos_y = array(1, 2, 2, 1, -1, -2, -2, -1);

// Recorre todas las casillas del tablero
for ($i = 0; $i < $n * $n - 1; $i++) {
    // Encuentra el próximo movimiento válido
    $siguiente_x = -1;
    $siguiente_y = -1;
    $mejor_movimiento = -1;
    for ($j = 0; $j < 8; $j++) {
        $nx = $x + $movimientos_x[$j];
        $ny = $y + $movimientos_y[$j];
        if ($nx >= 0 && $ny >= 0 && $nx < $n && $ny < $n && $tablero[$nx][$ny] == 0) {
            // Cuenta los movimientos posibles desde el próximo movimiento
            $movimientos_posibles = 0;
            for ($k = 0; $k < 8; $k++) {
                $nnx = $nx + $movimientos_x[$k];
                $nny = $ny + $movimientos_y[$k];
                if ($nnx >= 0 && $nny >= 0 && $nnx < $n && $nny < $n && $tablero[$nnx][$nny] == 0) {
                    $movimientos_posibles++;
                }
            }
            if ($siguiente_x == -1 || $movimientos_posibles < $mejor_movimiento) {
                $siguiente_x = $nx;
                $siguiente_y = $ny;
                $mejor_movimiento = $movimientos_posibles;
            }
        }
    }

    // Si no hay ningún movimiento válido, el ciclo hamiltoniano ha terminado
    if ($siguiente_x == -1) {
        break;
    }

    // Marca el próximo movimiento y actualiza la posición del caballo
    $movimiento++;
    $tablero[$siguiente_x][$siguiente_y] = $movimiento;
    $x = $siguiente_x;
    $y = $siguiente_y;
}

// Imprime el tablero con los movimientos del caballo numerados
echo "<table border='1'>";
for ($i = 0; $i < $n; $i++) {
    echo "<tr>";
    for ($j = 0; $j < $n; $j++) {
        echo "<td align='center' width='50' height='50'>";
        echo $tablero[$i][$j];
        echo "</td>";
    }
    echo "</tr>";
}
echo "</table>";
