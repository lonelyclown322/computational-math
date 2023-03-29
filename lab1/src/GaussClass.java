import java.lang.Math;
import java.math.BigDecimal;
import java.util.ArrayList;
import java.util.BitSet;
import java.util.Collections;
import java.util.List;

public class GaussClass { //Решение уравнений методом Гаусса

    public static double getTriangeMatrixDeterminant(List<List<Double>> matrix) {
        double det = 1;
        for (int i = 0; i < matrix.size(); i++) {
            det *= matrix.get(i).get(i);
        }

        return det;
    }

    public static List<Double> getRootsNew(List<List<Double>> triangleMatrix) {
        List<Double> result = new ArrayList<>();
        for (int i = triangleMatrix.size() - 1; i >= 0; i--) {
            Double res = triangleMatrix.get(i).get(triangleMatrix.size());
            for (int j = 0; j < triangleMatrix.size() - 1 - i; j++) {
                res += -triangleMatrix.get(i).get(triangleMatrix.size() - 1 - j) * result.get(j);
            }
            result.add(res / triangleMatrix.get(i).get(i));
        }
        Collections.reverse(result);
        return result;
    }

    public static List<BigDecimal> getMismatch(List<List<Double>> matrix, List<Double> roots) {

        List<BigDecimal> answer = new ArrayList<>();

        for (int i = 0; i < matrix.size(); i++) {
            BigDecimal r = new BigDecimal(Double.toString(matrix.get(i).get(matrix.size())));
            for (int j = 0; j < matrix.size(); j++) {
                r = r.subtract(
                        new BigDecimal(Double.toString(matrix.get(i).get(j)))
                                .multiply(new BigDecimal(Double.toString(roots.get(j))))
                );
            }

            answer.add(r);
        }
        return answer;
    }

    public static List<List<Double>> getTriangleMatrix(List<List<Double>> matrix, Integer newCounter) {

        Double determinant = 1.0;

        int counter = 0;

        newCounter = 0;

        List<List<Double>> triangleMatrix = new ArrayList<>();

        for (int i = 0; i < matrix.size(); i++) {
            triangleMatrix.add(new ArrayList<>(matrix.get(i)));
        }

        for (int i = 0; i < triangleMatrix.size(); i++) {
            Double maxColumnValue = 0.0;
            int maxValueAddress = i;
            for (int j = i; j < triangleMatrix.size(); j++) {
                if (Math.abs(triangleMatrix.get(j).get(i)) > maxColumnValue) {
                    maxColumnValue = Math.abs(triangleMatrix.get(j).get(i));
                    maxValueAddress = j;
                }
            }

            if (maxColumnValue == 0) {
                return null;
            }

            if (maxValueAddress != i) {
                newCounter++;
                List<Double> temp;
                temp = triangleMatrix.get(i);
                triangleMatrix.set(i, triangleMatrix.get(maxValueAddress));
                triangleMatrix.set(maxValueAddress, temp);
                counter++;
            }

//            determinant *= triangleMatrix.get(i).get(i);

//            for (int j = triangleMatrix.size(); j >= i; j--) {
//                triangleMatrix.get(i)
//                        .set(j, triangleMatrix.get(i).get(j) / triangleMatrix.get(i).get(i));
//            }

//            for (int j = triangleMatrix.size(); j >= i; j--) {
//                triangleMatrix.get(i)
//                        .set(j, triangleMatrix.get(i).get(j) / triangleMatrix.get(i).get(i));
//            }

            for (int y = i + 1; y < triangleMatrix.size(); y++) {
                for (int x = triangleMatrix.size(); x >= i; x--) {
                    triangleMatrix
                            .get(y)
                            .set(x, triangleMatrix.get(y).get(x) -
                                    triangleMatrix.get(y).get(i) * triangleMatrix.get(i).get(x) / triangleMatrix.get(i).get(i));
                }
            }

        }

        if (counter % 2 != 0) {
            determinant *= -1;
        }

//        System.out.println("axaxa");

//        System.out.println("Определитель");
//        System.out.println(determinant);

        System.out.println("Количество перестановок");
        System.out.println(newCounter);

        return triangleMatrix;
    }
}
