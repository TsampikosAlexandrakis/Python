stroke = float(input("Δώσε μήκος διαδρομής : "))
bore = float(input("Δώσε διάμετρο κυλινδρου : "))
cyl = float(input("Δώσε αριθμό κυλίνδρων : "))

displacement = (0.785 * bore**2 * stroke * cyl) /1000

print("Είναι",round(displacement,1),"κυβικά εκατοστά")
input()
