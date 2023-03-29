import java.io.*;
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {

    private static String inputType = "Введите 0, чтобы ввести данные с клавиатуры, 1 - чтобы ввести данные из файла.";
    private static String matrixSizeInput = "Укажите размерносить матрицы: ";
    private static String matrixElementsInput = "Введите все коэффициенты матрицы, начиная с первой строки, разделяя их пробелом";
    private static String givenMatrix = "Исходная матрица:";
    private static String calculatedTriangleMatrix = "Полученная треугольная матрица:";
    private static String triangleMatrixDeterminant = "Определитель треугольной матрицы:";
    private static String triangleNull = "Определитель матрицы равен 0\nСистема не имеет решений или их бесконечно много!";
    private static String rootsMessage = "Получены следующие корни системы:";
    private static String mismatchMessage = "Получен вектор невязки:";

    private static void print(Object s) {
        System.out.println(s);
    }

    private static void printMatrix(List<List<Double>> matrix) {
        for (int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j < matrix.size() + 1; j++) {
                System.out.print(matrix.get(i).get(j));
                System.out.print(' ');
            }
            System.out.println();
        }
    }

    private static void printRoots(List<Double> roots) {
        for (Double r : roots) {
//            System.out.printf("%.30f", r);
            System.out.printf("%.4f", r);
            System.out.print(' ');
        }

        System.out.println();
    }
    private static void printMismatch(List<BigDecimal> roots) {
        for (BigDecimal r : roots) {
            System.out.print(r);
            System.out.print(' ');
        }

        System.out.println();
    }


    public static void main(String[] args) throws IOException {
        int matrixSize = 0;
        List<List<Double>> matrix = new ArrayList<>();

        Scanner sc = new Scanner(System.in);

        print(inputType);

        int inputType = sc.nextInt();

        if (inputType == 0) {
            print(matrixSizeInput);

            matrixSize = sc.nextInt();

            print(matrixElementsInput);

            for (int i = 0; i < matrixSize; i++) {
                List<Double> row = new ArrayList<>();
                for (int j = 0; j < matrixSize + 1; j++) {
                    row.add(sc.nextDouble());
                }
                matrix.add(row);
            }
        }

        if (inputType == 1) {
            File file = new File("resources/input.txt");
            BufferedReader br
                    = new BufferedReader(new FileReader(file));
            String st;
            while ((st = br.readLine()) != null) {
                List<Double> row = new ArrayList<>();
                String[] tmp = st.split(" ");
                for (String s : tmp) {
                    row.add(Double.parseDouble(s));
                }
                matrix.add(row);
                matrixSize++;
            }
        }

        Integer numberOf = 0;

        List<List<Double>> triangleMatrix = GaussClass.getTriangleMatrix(matrix, numberOf);

        if (triangleMatrix == null) {
            print(triangleNull);
            return;
        }

        double det = GaussClass.getTriangeMatrixDeterminant(triangleMatrix);

        if (numberOf % 2 == 1) {
            det *= -1;
        }

        List<Double> roots = GaussClass.getRootsNew(triangleMatrix);

        List<BigDecimal> mismatch = GaussClass.getMismatch(matrix, roots);


        print(givenMatrix);
        printMatrix(matrix);
        print("");
        print(calculatedTriangleMatrix);
        printMatrix(triangleMatrix);
        print("");
        print(triangleMatrixDeterminant);
        print(det);
        print("");
        print(rootsMessage);
        printRoots(roots);
        print("");
        print(mismatchMessage);
        printMismatch(mismatch);


////        double[][] mtx = new double[matrixSize][matrixSize + 1];
////        double[][] mtxCopy = new double[matrixSize][matrixSize + 1];
////        int index = 0;
////        for (int i = 0; i < matrixSize; i++)
////            for (int j = 0; j < matrixSize + 1; j++) {
////                mtx[i][j] = mtxCopy[i][j] = matrix.get(index);
////                index++;
////            }
//
//
////        GaussClass.printMtx(mtxCopy);
////        GaussClass.setIndexMass(matrixSize);
////        double[][] triangleMtx = GaussClass.getTriangleNew(mtx);
////        if (triangleMtx != null) {
////            System.out.println("Получена треугольная матрица: ");
////            GaussClass.printMtx(triangleMtx);
////
////            System.out.println("Определитель матрицы равен: ");
////            double det = GaussClass.getDeterminant(triangleMtx);
////            System.out.println(det);
////            System.out.println();
////
////            if (det != 0) {
////                double[] x = GaussClass.getRootsNew(triangleMtx);
////                System.out.println("Найдены корни СЛАУ:");
////                for (double v : x) System.out.printf("%.2f\t", v);
////                System.out.println();
////                System.out.println();
////
////                System.out.println("Вектор невязки: ");
////                double[] dis = GaussClass.getDiscrepancyNew(mtxCopy, x);
////                for (double di : dis) System.out.printf("%.2f\t", di);
////                System.out.println();
////
////            } else System.out.println("Система имеет бесконечное множество решений!");
////        } else System.out.println("Ошибка в подсчете матрицы или система не имеет решений!");
//
    }
}