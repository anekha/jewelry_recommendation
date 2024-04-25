
def recommendation_results(recommendations):
    """
    Prints the results of jewelry recommendations based on the analysis of facial features and skin undertones.

    Parameters:
    - recommendations (dict): A dictionary containing all recommendation data.

    Outputs:
    - Printed statements summarizing the recommendations and analysis results.
    """
    # Extract face shape from recommendations and convert to lowercase
    face_shape = recommendations.get("face_shape")
    if face_shape:
        face_shape = face_shape.lower()
        print("Face shape:", face_shape)
    else:
        print("No face shape detected.")

    # Print undertone classification
    print("Undertone Classification:", recommendations.get("undertone"))

    # Display color data and the color block if available
    if recommendations.get("hist") is not None and recommendations.get("colors") is not None:
        if recommendations["hist"].size > 0 and recommendations["colors"].size > 0:
            print("Dominant Colors:")
            for i, (percent, color) in enumerate(zip(recommendations["hist"], recommendations["colors"])):
                color_name = f"Color {i+1}"
                color_rgb = f"RGB: ({', '.join(map(str, color.astype('int').tolist()))})"
                print(f"  {color_name}: {color_rgb} - {percent:.2%}")

            # Assuming display_color_block is imported from color_analysis
            from color_analysis import display_color_block
            display_color_block(recommendations["colors"], recommendations["hist"])
        else:
            print("No color data available.")
    else:
        print("No color data available.")

    # Print jewelry recommendations
    print("\nJewelry Recommendations:")
    print("- Jewelry Design:", recommendations.get("jewelry_design"))
    print("- Gemstone Shape:", recommendations.get("gemstone_shape"))
    print("- Gemstone Recommendation:", recommendations.get("gemstone_recommendation"))
    print("- Metal Color Recommendation:", recommendations.get("metal_color_recommendation"))
