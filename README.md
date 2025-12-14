🌱 Eco-Footprint Analyzer

A modern, interactive Python desktop application designed to raise awareness about the environmental cost of food consumption. This tool calculates the Carbon Footprint (CO2​) and Virtual Water Usage of a grocery shopping list in real-time.

    Note: This application was developed as an Environmental Studies (EVS) Project to visualize the hidden costs of everyday food items.

📸 Features

    Interactive Dashboard: Built with CustomTkinter for a modern, dark-mode UI.

    Real-time Calculations: Instantly updates total Carbon (kg) and Water (L) usage as items are added.

    Visual Analytics: Embedded Matplotlib bar chart to compare impacts visually (Water consumption is scaled down by 100 for better graph comparison).

    Shopping List History: Keeps track of added items in a scrollable list.

    Educational Info: Includes a "Did You Know?" section about Virtual Water.

🛠️ Installation & Requirements

Ensure you have Python installed. You will need to install the external libraries used for the GUI and plotting.

    Clone or Download this repository.

    Install dependencies using pip:

Bash

pip install customtkinter matplotlib

(Note: tkinter is usually included with standard Python installations).
🚀 How to Run

    Navigate to the project directory in your terminal/command prompt.

    Run the script:

Bash

python main.py

(Replace main.py with whatever you named the python file).
📊 How it Works

    Select an Item: Use the dropdown menu in the sidebar to choose a food category (e.g., Beef, Rice, Coffee).

    Enter Quantity: Type the amount in kilograms (or Liters for milk).

    Add to List: Click the "+ Add to List" button.

    View Results:

        The Shopping List updates with your item.

        The Metric Cards update the total Environmental Impact.

        The Graph dynamically adjusts to show the new data.

    Reset: Click "Reset All" to clear the data and start over.

📋 Data Source (Impact Factors)

The application uses the following approximate values for calculation:
Food Item	Unit	Carbon Emission (kg CO2)	Virtual Water (L)
Beef (Meat)	1 kg	99.48	15,415
Chicken (Meat)	1 kg	9.87	4,325
Rice (Grain)	1 kg	4.45	2,497
Milk (Dairy)	1 L	3.00	1,020
Cheese	1 kg	23.88	5,605
Vegetables	1 kg	0.40	322
Coffee	1 kg	28.50	18,900
Chocolate	1 kg	46.60	17,196
🧩 Project Structure

    EcoApp Class: The main entry point inheriting from ctk.CTk. Handles window setup and geometry.

    DATA_DB Dictionary: Stores the environmental data constants.

    init_chart Function: Embeds the Matplotlib figure into the Tkinter window.

    update_display Function: Refreshes the text boxes, labels, and redraws the graph canvas.

📜 License

This project is open-source and free to use for educational purposes.