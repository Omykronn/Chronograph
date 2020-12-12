from bokeh.plotting import figure, output_file, show
from bokeh.models import Arrow, VeeHead, Legend, LegendItem
from MathOperation.polynomial import Polynomial


pos_color = "blue"  # Color of the Position Points
speed_color = "green"  # Color of the Speed Vectors
acc_color = "red"  # Color of the Acceleration Vectors

var = input("Used Variable >>> ")  # Name of the used Variable
nb = int(input("Number of Point to draw >>> "))

equX = Polynomial(input("Movement's Equation of X-Axis >>> "), var)  # Equation of the Movement on the X-Axis
equY = Polynomial(input("Movement's Equation of Y-Axis >>> "), var)  # Equation of the Movement on the Y-Axis

speed_x = equX.derive()  # Equation of the X-Speed Value
speed_y = equY.derive()  # Equation of the Y-Speed Value

acc_x = speed_x.derive()  # Equation of the X-Acceleration Value
acc_y = speed_y.derive()  # Equation of the Y-Acceleration Value

range_t = [i / 10 for i in range(nb * 10)]

pos_x = eval("[{equ} for {var} in {range}]".format(equ=equX, var=var, range=range_t))  # Calculate the X Position
pos_y = eval("[{equ} for {var} in {range}]".format(equ=equY, var=var, range=range_t))  # Calculate the Y Position

# Calculate the Speed Vector's Coordinates
speed_vector = eval("[({x}, {y}) for {var} in range({max})]".format(x=speed_x, y=speed_y, var=var, max=nb))

# Calculate the Acceleration Vector's Coordinates
acc_vector = eval("[({x}, {y}) for {var} in range({max})]".format(x=acc_x, y=acc_y, var=var, max=nb))

# HTML File Exporting
output_file("Mechanic_Movement.html", title="Chromatograph")

# Creation of the Canvas
f = figure(sizing_mode="stretch_both", x_axis_label="x(t) = " + equX.format(), y_axis_label="y(t) = " + equY.format(),
           tools="box_zoom,wheel_zoom,reset,save")

# Draw each Point of the Movement
f.line(pos_x, pos_y, width=2, color=pos_color, name="pos")
f.circle([pos_x[10*i] for i in range(nb)], [pos_y[10*i] for i in range(nb)], size=10, color=pos_color, name="pos")

# Drawing of each Speed and Acceleration Vectors
for i in range(nb):
    f.add_layout(Arrow(end=VeeHead(size=10, line_color=speed_color, fill_color=speed_color), line_color=speed_color,
                       line_width=2, x_start=pos_x[10*i], y_start=pos_y[10*i], x_end=pos_x[10*i] + speed_vector[i][0],
                       y_end=pos_y[10*i] + speed_vector[i][1]))  # Draw the Speed Vector at Point i+1

    f.add_layout(Arrow(end=VeeHead(size=10, line_color=acc_color, fill_color=acc_color), line_color=acc_color,
                       line_width=2, x_start=pos_x[10*i], y_start=pos_y[10*i], x_end=pos_x[10*i] + acc_vector[i][0],
                       y_end=pos_y[10*i] + acc_vector[i][1]))  # Draw the Acceleration Vector at Point i+1

# Creating the Legend
f.add_layout(Legend(items=[LegendItem(label="Trajectory", renderers=f.select(name="pos")),
                           LegendItem(label="Speed Vector (m/s)", renderers=[f.line(color=speed_color, line_width=2)]),
                           LegendItem(label="Acceleration Vector (m/s²)", renderers=[f.line(color=acc_color, line_width=2)])]))

show(f)
