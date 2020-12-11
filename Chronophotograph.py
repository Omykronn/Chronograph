from bokeh.plotting import figure, output_file, show
from bokeh.models import Arrow, VeeHead


nb = 5  # Number of Point
var = "t"  # Name of the used Variable

equX = "2 * t**2 + t"  # Equation of the Movement on the X-Axis
equY = "t**3 + 2*t**2 + 3*t + 4"  # Equation of the Movement on the Y-Axis

speed_x = "4**t + 1"  # Equation of the X-Speed Value
speed_y = "3*t**2 + 4*t + 3"  # Equation of the Y-Speed Value

acc_x = "5"  # Equation of the X-Acceleration Value
acc_y = "6*t + 4"  # Equation of the Y-Acceleration Value

# ------ END OF THE EDITABLE PARAMETER ------

pos_color = "blue"  # Color of the Position Points
speed_color = "green"  # Color of the Speed Vectors
acc_color = "red"  # Color of the Acceleration Vectors

pos_x = eval("[{equ} for {var} in range({max})]".format(equ=equX, var=var, max=nb))  # Calculate the X Position
pos_y = eval("[{equ} for {var} in range({max})]".format(equ=equY, var=var, max=nb))  # Calculate the Y Position

# Calculate the Speed Vector's Coordinates
speed_vector = eval("[({x}, {y}) for {var} in range({max})]".format(x=speed_x, y=speed_y, var=var, max=nb))

# Calculate the Acceleration Vector's Coordinates
acc_vector = eval("[({x}, {y}) for {var} in range({max})]".format(x=acc_x, y=acc_y, var=var, max=nb))

# HTML File Exporting
output_file("Mechanic_Movement.html", title="Chromatograph")

# Creation of the Canvas
f = figure(plot_width=1900, plot_height=950, x_range=[-1, pos_x[-1] + speed_vector[-1][0] + 2],
           y_range=[-1, pos_y[-1] + speed_vector[-1][1] + 2], tools="box_zoom,wheel_zoom,reset")

f.circle(pos_x, pos_y, size=10, color=pos_color)  # Draw each Point of the Movement


# Drawing of each Speed and Acceleration Vectors
for i in range(nb):
    f.add_layout(Arrow(end=VeeHead(size=10, line_color=speed_color, fill_color=speed_color), line_color=speed_color,
                       line_width=2, x_start=pos_x[i], y_start=pos_y[i], x_end=pos_x[i] + speed_vector[i][0],
                       y_end=pos_y[i] + speed_vector[i][1]))  # Draw the Speed Vector at Point i+1

    f.add_layout(Arrow(end=VeeHead(size=10, line_color=acc_color, fill_color=acc_color), line_color=acc_color,
                       line_width=2, x_start=pos_x[i], y_start=pos_y[i], x_end=pos_x[i] + acc_vector[i][0],
                       y_end=pos_y[i] + acc_vector[i][1]))  # Draw the Acceleration Vector at Point i+1

show(f)
