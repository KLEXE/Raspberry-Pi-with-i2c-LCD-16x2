import   lcddriver     
        import   time     
        import   datetime     
        # Load   the driver and set it to "display"     
        # If   you use something from the driver library use the "display." prefix   first     
        display   = lcddriver.lcd ()     
        try:     
            Print ("Writing to display")     
            display.lcd_display_string ("No time   to waste", 1) # Write line of text to first line of display     
            while True:     
                display.lcd_display_string (str (datetime.datetime.now   (). time ()), 2) # Write just the time to the display     
                # Program then loops with no delay   (Can be added with a time.sleep)     
        except   KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c),   exit the program and cleanup     
            Print ("Cleaning up!")     
            display.lcd_clear ()   