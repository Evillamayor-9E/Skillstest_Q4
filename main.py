from pyscript import display # pyright: ignore[reportMissingImports]
import numpy as np
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

import matplotlib.pyplot as pit

days = np.array(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])
sales = np.array([0, 2, 4, 6, 8])
emerald_sales = pit.plot(days, sales) #pit.bar pit.plot pit.barh

pit.show()
pit.title('Weekly Attendance (Absences)')
pit.xlabel('DAYS')
pit.ylabel('NUMBER OF ABSENCES')