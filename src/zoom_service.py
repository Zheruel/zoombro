import os
from playwright.sync_api import sync_playwright


def join_zoom_call(zoom_link, name, file_name, stdscr, headless=False):
    with sync_playwright() as playwright:
        stdscr.addstr(4, 0, "Getting ready to join the call...")
        stdscr.refresh()

        file_path = os.path.join(os.getcwd(), "videos", file_name)
        browser = playwright.chromium.launch(headless=headless, args=["--use-fake-ui-for-media-stream",
                                                                      "--use-fake-device-for-media-stream",
                                                                      f"--use-file-for-fake-video-capture={file_path}"])
        context = browser.new_context()
        page = context.new_page()
        page.goto(zoom_link)

        # Close the cookie banner
        close_button = page.wait_for_selector(
            ".onetrust-close-btn-handler.onetrust-close-btn-ui.banner-close-button.ot-close-icon")
        close_button.click()
        stdscr.addstr(5, 0, "Step 1 of 5 complete...")
        stdscr.refresh()

        # Mute yourself
        mic_button = page.wait_for_selector("#mic-btn")
        mic_button.click()
        stdscr.addstr(6, 0, "Step 2 of 5 complete...")
        stdscr.refresh()

        # Put in the name
        name_field = page.wait_for_selector(".form-control.input-lg")
        name_field.fill(name)
        stdscr.addstr(7, 0, "Step 3 of 5 complete...")
        stdscr.refresh()

        # Join the call
        join_button = page.wait_for_selector("#joinBtn")
        join_button.click()
        stdscr.addstr(8, 0, "Step 4 of 5 complete...")
        stdscr.refresh()

        # Agree to the terms
        agree_button = page.wait_for_selector("#wc_agree1")
        agree_button.click()
        stdscr.addstr(9, 0, "Step 5 of 5 complete...")
        stdscr.refresh()

        stdscr.addstr(10, 0, "Bot has successfully joined the call!")
        stdscr.refresh()

        page.wait_for_timeout(600000)
