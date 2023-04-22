import flet as ft
from flet import IconButton, Page, Row, TextField, icons, ElevatedButton, Image
from predict_multi import predict
from chart import makechart
from chord import predict_chord
import os
import cv2
import time

def main(page: Page):
    page.title = "RecChord"
    page.vertical_alignment = "center"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "bluegrey"
    page.padding=-10
    b = ft.Image(
                    src=os.path.join(os.path.abspath(os.curdir),'assets/bg4.jpg'),
                    width=1800,
                    height=892,
                    fit=ft.ImageFit.CONTAIN,
                )
    

    im_404 = Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/404.png'),
            width = 700,
            fit='fitWidth',
            visible=False,
        )
    def rec_click(e):
        if not isinstance(pick_file_path.value,str) or pick_file_path.value == "Cancelled!":
            page.dialog = dlg_modal
            dlg_modal.open = True
            page.update()
        else:
            back_button.disabled = True
            file_button.disabled = True
            rec_button.disabled = True
            photo_button.disabled = True
            for i in range(len(lv.controls)):
                lv.controls.remove(lv.controls[0])
            pr.visible = True
            page.update()
            # page.add(pr)
            predict(pick_file_path.value, set5.value)
            makechart("temp")
            # chord.value = predict_chord('result/harmony.csv')
            # chord.update()
            # page.remove(pr)
            chordlist = predict_chord('temp/harmony.csv', set2.value)
            pr.visible = False
            # for i in range(len(lv.controls)):
            #     lv.controls.remove(lv.controls[0])
            A7_button = ft.TextButton(text='A7', on_click=A7_click)
            Am7_button = ft.TextButton(text='Am7', on_click=Am7_click)
            Ab7_button = ft.TextButton(text='Ab7', on_click=Ab7_click)
            A75_button = ft.TextButton(text='A7#7', on_click=A75_click)
            Ab_button = ft.TextButton(text='Ab', on_click=Ab_click)
            Ao7_button = ft.TextButton(text='Ao7', on_click=Ao7_click)
            Bb_button = ft.TextButton(text='Bb', on_click=Bb_click)
            B7_button = ft.TextButton(text='B7', on_click=B7_click)
            Bbm7_button = ft.TextButton(text='Bbm7', on_click=Bbm7_click)
            Bb7_button = ft.TextButton(text='Bb7', on_click=Bb7_click)
            Bm7_button = ft.TextButton(text='Bm7', on_click=Bm7_click)
            Bo7_button = ft.TextButton(text='Bo7', on_click=Bo7_click)
            C_button = ft.TextButton(text='C', on_click=C_click)
            C6_button = ft.TextButton(text='C6', on_click=C6_click)
            C7_button = ft.TextButton(text='C7', on_click=C7_click)
            Cm7_button = ft.TextButton(text='Cm7', on_click=Cm7_click)
            D7_button = ft.TextButton(text='D7', on_click=D7_click)
            D7b7_button = ft.TextButton(text='D7b7', on_click=D7b7_click)
            Db_button = ft.TextButton(text='Db', on_click=Db_click)
            Db7_button = ft.TextButton(text='Db7', on_click=Db7_click)
            Dm7_button = ft.TextButton(text='Dm7', on_click=Dm7_click)
            E7_button = ft.TextButton(text='E7', on_click=E7_click) 
            Eb_button = ft.TextButton(text='Eb', on_click=Eb_click)
            Eb7_button = ft.TextButton(text='Eb7', on_click=Eb7_click)
            Ebm7_button = ft.TextButton(text='Ebm7', on_click=Ebm7_click)
            Em7_button = ft.TextButton(text='Em7', on_click=Em7_click)
            Eo7_button = ft.TextButton(text='Eo7', on_click=Eo7_click)
            F_button = ft.TextButton(text='F', on_click=F_click)
            F6_button = ft.TextButton(text='F6', on_click=F6_click)
            F7_button = ft.TextButton(text='F7', on_click=F7_click)
            Fm7_button = ft.TextButton(text='Fm7', on_click=Fm7_click)
            G_button = ft.TextButton(text='G', on_click=G_click)
            G6_button = ft.TextButton(text='G6', on_click=G6_click)
            G7_button = ft.TextButton(text='G7', on_click=G7_click)
            G7b7_button = ft.TextButton(text='G7b7', on_click=G7b7_click)
            Gm7_button = ft.TextButton(text='Gm7', on_click=Gm7_click)
            count = 0
            for i in chordlist:
                if i == '&':
                    lv.visible = False
                    c1.visible = False
                    im_404.visible = True
                    break
                else:
                    lv.visible = True
                    c1.visible = True
                    count += 1
                    if len(i.split(",")) != 1:
                        buttons = []
                        temp = i.split(",")
                        for j in temp:
                            if j == 'A7':
                                buttons.append(A7_button)
                            elif j == 'Am7':
                                buttons.append(Am7_button)
                            elif j == 'Ab7':
                                buttons.append(Ab7_button)
                            elif j == 'A7#5':
                                buttons.append(A75_button)
                            elif j == 'Ab':
                                buttons.append(Ab_button)
                            elif j == 'Ao7':
                                buttons.append(Ao7_button)
                            elif j == 'Bb':
                                buttons.append(Bb_button)
                            elif j == 'B7':
                                buttons.append(B7_button)
                            elif j == 'Bbm7':
                                buttons.append(Bbm7_button)
                            elif j == 'Bb7':
                                buttons.append(Bb7_button)
                            elif j == 'Bm7':
                                buttons.append(Bm7_button)
                            elif j == 'Bo7':
                                buttons.append(Bo7_button)
                            elif j == 'C':
                                buttons.append(C_button)
                            elif j == 'C6':
                                buttons.append(C6_button)
                            elif j == 'C7':
                                buttons.append(C7_button)
                            elif j == 'Cm7':
                                buttons.append(Cm7_button)
                            elif j == 'D7':
                                buttons.append(D7_button)
                            elif j == 'D7b7':
                                buttons.append(D7b7_button)
                            elif j == 'Db':
                                buttons.append(Db_button)
                            elif j == 'Db7':
                                buttons.append(Db7_button)
                            elif j == 'Dm7':
                                buttons.append(Dm7_button)
                            elif j == 'E7':
                                buttons.append(E7_button)
                            elif j == 'Eb':
                                buttons.append(Eb_button)
                            elif j == 'Eb7':
                                buttons.append(Eb7_button)
                            elif j == 'Ebm7':
                                buttons.append(Ebm7_button)
                            elif j == 'Em7':
                                buttons.append(Em7_button)
                            elif j == 'Eo7':
                                buttons.append(Eo7_button)
                            elif j == 'F':
                                buttons.append(F_button)
                            elif j == 'F6':
                                buttons.append(F6_button)
                            elif j == 'F7':
                                buttons.append(F7_button)
                            elif j == 'Fm7':
                                buttons.append(Fm7_button)
                            elif j == 'G':
                                buttons.append(G_button)
                            elif j == 'G6':
                                buttons.append(G6_button)
                            elif j == 'G7':
                                buttons.append(G7_button)
                            elif j == 'G7b7':
                                buttons.append(G7b7_button)
                            else:
                                buttons.append(Gm7_button)
                        chord_img = Row([ft.Text('Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), buttons[0],ft.Text(' - ambiguity: (', style=ft.TextThemeStyle.BODY_LARGE, weight=ft.FontWeight.BOLD,), buttons[1], buttons[2], buttons[3],ft.Text(') ', style=ft.TextThemeStyle.BODY_LARGE, weight=ft.FontWeight.BOLD,),],alignment='center')
                    else:
                        if i == 'A7':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), A7_button,ft.Text(' '),],)
                        elif i == 'Am7':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), Am7_button,ft.Text(' '),],)
                        elif i == 'Ab7':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), Ab7_button,ft.Text(' '),],)
                        elif i == 'A7#5':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), A75_button,ft.Text(' '),],)
                        elif i == 'Ab':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), Ab_button,ft.Text(' '),],)
                        elif i == 'Ao7':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), Ao7_button,ft.Text(' '),],)
                        elif i == 'Bb':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), Bb_button,ft.Text(' '),],)
                        elif i == 'B7':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), B7_button,ft.Text(' '),],)
                        elif i == 'Bbm7':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), Bbm7_button,ft.Text(' '),],)
                        elif i == 'Bb7':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), Bb7_button,ft.Text(' '),],)
                        elif i == 'Bm7':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), Bm7_button,ft.Text(' '),],)
                        elif i == 'Bo7':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), Bo7_button,ft.Text(' '),],)
                        elif i == 'C':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), C_button,ft.Text(' '),],)
                        elif i == 'C6':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), C6_button,ft.Text(' '),],)
                        elif i == 'C7':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), C7_button,ft.Text(' '),],)
                        elif i == 'Cm7':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), Cm7_button,ft.Text(' '),],)
                        elif i == 'D7':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), D7_button,ft.Text(' '),],)
                        elif i == 'D7b7':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), D7b7_button,ft.Text(' '),],)
                        elif i == 'Db':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), Db_button,ft.Text(' '),],)
                        elif i == 'Db7':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), Db7_button,ft.Text(' '),],)
                        elif i == 'Dm7':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), Dm7_button,ft.Text(' '),],)
                        elif i == 'E7':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), E7_button,ft.Text(' '),],)
                        elif i == 'Eb':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), Eb_button,ft.Text(' '),],)
                        elif i == 'Eb7':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), Eb7_button,ft.Text(' '),],)
                        elif i == 'Ebm7':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), Ebm7_button,ft.Text(' '),],)
                        elif i == 'Em7':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), Em7_button,ft.Text(' '),],)
                        elif i == 'Eo7':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), Eo7_button,ft.Text(' '),],)
                        elif i == 'F':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), F_button,ft.Text(' '),],)
                        elif i == 'F6':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), F6_button,ft.Text(' '),],)
                        elif i == 'F7':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), F7_button,ft.Text(' '),],)
                        elif i == 'Fm7':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), Fm7_button,ft.Text(' '),],)
                        elif i == 'G':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), G_button,ft.Text(' '),],)
                        elif i == 'G6':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), G6_button,ft.Text(' '),],)
                        elif i == 'G7':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), G7_button,ft.Text(' '),],)
                        elif i == 'G7b7':
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), G7b7_button,ft.Text(' '),],)
                        else:
                            chord_img = Row([ft.Text('                                                Chord '+str(count)+':   ', weight=ft.FontWeight.BOLD, style=ft.TextThemeStyle.BODY_LARGE), Gm7_button,ft.Text(' '),],)
                    lv.controls.append(chord_img)
            # page.add(lv)
            back_button.disabled = False
            file_button.disabled = False
            rec_button.disabled = False
            photo_button.disabled = False
            page.update()

    def pick_file_result(e: ft.FilePickerResultEvent):
        # try:
        #     page.remove(lv)
        # except ValueError: pass
        pick_file_path.value = "Cancelled!"
        pick_file_path.value = e.path if e.path else "Cancelled!"
        im_404.visible = False
        # pick_file_path.update()
        if pick_file_path.value != "Cancelled!":
            c1.visible = True
            lv.visible = False
            myimg.src = e.path
            myimg.width = 1000
            myimg.height = 200
            page.update()
        else:
            c1.visible = False
            lv.visible = False
            myimg.src = os.path.join(os.path.abspath(os.curdir),'assets/cancle.png')
            myimg.width = 360
            myimg.height = 360
            page.update()

    def start_click(e):
        start_button.visible = False
        set_button.visible = False
        help_button.visible = False
        file_button.visible = True
        photo_button.visible = True
        rec_button.visible = True
        back_button.visible = True
        page.update()

    def set_click(e):
        start_button.visible = False
        set_button.visible = False
        help_button.visible = False
        myimg.visible = False
        back_button.visible = True

        set1.visible = True
        set2.visible = True
        set3.visible = True
        set4.visible = True
        set5.visible = True
        set6.visible = True
        set7.visible = True
        page.update()

    def help_click(e):
        start_button.visible = False
        set_button.visible = False
        help_button.visible = False
        myimg.visible = False
        back_button.visible = True

        help1.visible = True
        help2.visible = True
        help3.visible = True
        help31.visible = True
        help4.visible = True
        help5.visible = True
        help6.visible = True
        help7.visible = True
        help8.visible = True
        help9.visible = True
        help10.visible = True
        help11.visible = True
        page.update()

    def back_click(e):
        # remove the temp photos
        file_name = os.path.join(os.path.abspath(os.curdir),'temp')
        file_name_list = os.listdir(file_name)
        for f in file_name_list:
            os.remove(os.path.join(file_name,f))

        # for i in range(len(lv.controls)):
        #     lv.controls.remove(lv.controls[0])
        im_404.visible = False
        help1.visible = False
        help2.visible = False
        help3.visible = False
        help31.visible = False
        help4.visible = False
        help5.visible = False
        help6.visible = False
        help7.visible = False
        help8.visible = False
        help9.visible = False
        help10.visible = False
        help11.visible = False

        set1.visible = False
        set2.visible = False
        set3.visible = False
        set4.visible = False
        set5.visible = False
        set6.visible = False
        set7.visible = False

        lv.visible = False
        c1.visible = False
        pick_file_path.value = "Cancelled!"
        myimg.width = 650
        myimg.height = 350
        back_button.visible = False
        file_button.visible = False
        photo_button.visible = False
        rec_button.visible = False
        start_button.visible = True
        set_button.visible = True
        help_button.visible = True
        myimg.src = os.path.join(os.path.abspath(os.curdir),'assets/title2.png')
        myimg.visible = True
        page.update()

    def shell_click(e):
        page.launch_url('https://s3.amazonaws.com/kajabi-storefronts-production/sites/86048/downloads/4qnFomATQKrFghiT2f6i_Any_Jazz_Chord_by_Jared_Borkowski_V2_.pdf')

    def sample_click(e):
        page.dialog = help35
        help35.open = True
        page.update()
        
    def close_dlg(e):
        dlg_modal.open = False
        help35.open = False
        gm7_modal.open = False
        a7_modal.open = False
        am7_modal.open = False
        ab7_modal.open = False
        a75_modal.open = False
        ab_modal.open = False
        ao7_modal.open = False
        b7_modal.open = False
        bb_modal.open = False
        bb7_modal.open = False
        bbm7_modal.open = False
        bm7_modal.open = False
        bo7_modal.open = False
        c_modal.open = False
        c6_modal.open = False
        c7_modal.open = False
        cm7_modal.open = False
        d7_modal.open = False
        d7b7_modal.open = False
        db_modal.open = False
        db7_modal.open = False
        dm7_modal.open = False
        e7_modal.open = False
        eb_modal.open = False
        eb7_modal.open = False
        ebm7_modal.open = False
        em7_modal.open = False
        eo7_modal.open = False
        f_modal.open = False
        f6_modal.open = False
        f7_modal.open = False
        fm7_modal.open = False
        g_modal.open = False
        g6_modal.open = False
        g7_modal.open = False
        g7b7_modal.open = False

        gm7_audio.pause()
        a7_audio.pause()
        am7_audio.pause()
        ab7_audio.pause()
        a75_audio.pause()
        ab_audio.pause()
        ao7_audio.pause()
        b7_audio.pause()
        bb_audio.pause()
        bb7_audio.pause()
        bbm7_audio.pause()
        bm7_audio.pause()
        bo7_audio.pause()
        c_audio.pause()
        c6_audio.pause()
        c7_audio.pause()
        cm7_audio.pause()
        d7_audio.pause()
        d7b7_audio.pause()
        db_audio.pause()
        db7_audio.pause()
        dm7_audio.pause()
        e7_audio.pause()
        eb_audio.pause()
        eb7_audio.pause()
        ebm7_audio.pause()
        em7_audio.pause()
        eo7_audio.pause()
        f_audio.pause()
        f6_audio.pause()
        f7_audio.pause()
        fm7_audio.pause()
        g_audio.pause()
        g6_audio.pause()
        g7_audio.pause()
        g7b7_audio.pause()
        page.update()

    def slider_changed(e):
        set3.value = f"There will be {e.control.value}% ambiguity results"
        # print(set2.value)
        page.update()

    def theme_changed(e):
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        set7.label = (
            "Light theme" if page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        if page.theme_mode == ft.ThemeMode.DARK:
            b.src=os.path.join(os.path.abspath(os.curdir),'assets/bg2.jpg')
            b.width=2600
            b.height=770
        else:
            b.src=os.path.join(os.path.abspath(os.curdir),'assets/bg4.jpg')
            b.width=1800
            b.height=892

        page.update()

    # 920x500
    def Gm7_click(e):
        page.dialog = gm7_modal
        gm7_modal.open = True
        page.update()

    def A7_click(e):
        page.dialog = a7_modal
        a7_modal.open = True
        page.update()

    def Am7_click(e):
        page.dialog = am7_modal
        am7_modal.open = True
        page.update()

    def Ab7_click(e):
        page.dialog = ab7_modal
        ab7_modal.open = True
        page.update()

    def A75_click(e):
        page.dialog = a75_modal
        a75_modal.open = True
        page.update()

    def Ab_click(e):
        page.dialog = ab_modal
        ab_modal.open = True
        page.update()

    def Ao7_click(e):
        page.dialog = ao7_modal
        ao7_modal.open = True
        page.update()

    def B7_click(e):
        page.dialog = b7_modal
        b7_modal.open = True
        page.update()

    def Bb_click(e):
        page.dialog = bb_modal
        bb_modal.open = True
        page.update()

    def Bb7_click(e):
        page.dialog = bb7_modal
        bb7_modal.open = True
        page.update()

    def Bbm7_click(e):
        page.dialog = bbm7_modal
        bbm7_modal.open = True
        page.update()

    def Bm7_click(e):
        page.dialog = bm7_modal
        bm7_modal.open = True
        page.update()

    def Bo7_click(e):
        page.dialog = bo7_modal
        bo7_modal.open = True
        page.update()

    def C_click(e):
        page.dialog = c_modal
        c_modal.open = True
        page.update()

    def C6_click(e):
        page.dialog = c6_modal
        c6_modal.open = True
        page.update()

    def C7_click(e):
        page.dialog = c7_modal
        c7_modal.open = True
        page.update()

    def Cm7_click(e):
        page.dialog = cm7_modal
        cm7_modal.open = True
        page.update()

    def D7_click(e):
        page.dialog = d7_modal
        d7_modal.open = True
        page.update()

    def D7b7_click(e):
        page.dialog = d7b7_modal
        d7b7_modal.open = True
        page.update()

    def Db_click(e):
        page.dialog = db_modal
        db_modal.open = True
        page.update()

    def Db7_click(e):
        page.dialog = db7_modal
        db7_modal.open = True
        page.update()

    def Dm7_click(e):
        page.dialog = dm7_modal
        dm7_modal.open = True
        page.update()

    def E7_click(e):
        page.dialog = e7_modal
        e7_modal.open = True
        page.update()

    def Eb_click(e):
        page.dialog = eb_modal
        eb_modal.open = True
        page.update()

    def Eb7_click(e):
        page.dialog = eb7_modal
        eb7_modal.open = True
        page.update()

    def Ebm7_click(e):
        page.dialog = ebm7_modal
        ebm7_modal.open = True
        page.update()

    def Em7_click(e):
        page.dialog = em7_modal
        em7_modal.open = True
        page.update()

    def Eo7_click(e):
        page.dialog = eo7_modal
        eo7_modal.open = True
        page.update()

    def F_click(e):
        page.dialog = f_modal
        f_modal.open = True
        page.update()

    def F6_click(e):
        page.dialog = f6_modal
        f6_modal.open = True
        page.update()

    def F7_click(e):
        page.dialog = f7_modal
        f7_modal.open = True
        page.update()

    def Fm7_click(e):
        page.dialog = fm7_modal
        fm7_modal.open = True
        page.update()

    def G_click(e):
        page.dialog = g_modal
        g_modal.open = True
        page.update()

    def G6_click(e):
        page.dialog = g6_modal
        g6_modal.open = True
        page.update()

    def G7_click(e):
        page.dialog = g7_modal
        g7_modal.open = True
        page.update()

    def G7b7_click(e):
        page.dialog = g7b7_modal
        g7b7_modal.open = True
        page.update()

    def photo_click(e):
        for i in range(len(lv.controls)):
            lv.controls.remove(lv.controls[0])
        lv.visible = False
        c1.visible = False
        photo_button.disabled = True
        file_button.disabled = True
        back_button.disabled = True
        rec_button.disabled = True
        page.update()
        cap = cv2.VideoCapture(0)

        timestamp = str(int(time.time()))
        hehehe = 'temp/photo'+timestamp+'.jpg'
        try:
            while True:
                ret, frame = cap.read()
                cv2.imshow('camera input',frame)
                key = cv2.waitKey(1)
                if key == 27:
                    break
                elif key == 32:
                    pick_file_path.value = os.path.join(os.path.abspath(os.curdir),hehehe)
                    cv2.imwrite(os.path.join(os.path.abspath(os.curdir),hehehe),frame)
                    myimg.src = os.path.join(os.path.abspath(os.curdir),hehehe)
                    myimg.width = frame.shape[1]* 0.6
                    myimg.height = frame.shape[0] * 0.6
                    page.update()
                    break
            photo_button.disabled = False
            file_button.disabled = False
            back_button.disabled = False
            rec_button.disabled = False
            cap.release()
            cv2.destroyAllWindows()
            page.update()
        except:
            print(e)
            pass


    gm7_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/gm7.mp3'), autoplay=False)

    gm7_row = Row([ft.Text('Gm7'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: gm7_audio.play()),],)

    gm7_modal = ft.AlertDialog(
        modal=True,
        title=gm7_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/gm7.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    a7_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/a7.mp3'), autoplay=False)

    a7_row = Row([ft.Text('A7'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: a7_audio.play()),],)

    a7_modal = ft.AlertDialog(
        modal=True,
        title=a7_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/a7.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    am7_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/am7.mp3'), autoplay=False)

    am7_row = Row([ft.Text('Am7'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: am7_audio.play()),],)

    am7_modal = ft.AlertDialog(
        modal=True,
        title=am7_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/am7.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    ab7_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/ab7.mp3'), autoplay=False)

    ab7_row = Row([ft.Text('Ab7'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: ab7_audio.play()),],)

    ab7_modal = ft.AlertDialog(
        modal=True,
        title=ab7_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/ab7.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    a75_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/a7#5.mp3'), autoplay=False)

    a75_row = Row([ft.Text('A7#5'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: a75_audio.play()),],)

    a75_modal = ft.AlertDialog(
        modal=True,
        title=a75_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/a7#5.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    ab_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/ab.mp3'), autoplay=False)

    ab_row = Row([ft.Text('Ab'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: ab_audio.play()),],)

    ab_modal = ft.AlertDialog(
        modal=True,
        title=ab_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/ab.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    ao7_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/ao7.mp3'), autoplay=False)

    ao7_row = Row([ft.Text('Ao7'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: ao7_audio.play()),],)

    ao7_modal = ft.AlertDialog(
        modal=True,
        title=ao7_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/ao7.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    b7_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/b7.mp3'), autoplay=False)

    b7_row = Row([ft.Text('B7'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: b7_audio.play()),],)

    b7_modal = ft.AlertDialog(
        modal=True,
        title=b7_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/b7.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    bb_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/bb.mp3'), autoplay=False)

    bb_row = Row([ft.Text('Bb'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: bb_audio.play()),],)

    bb_modal = ft.AlertDialog(
        modal=True,
        title=bb_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/bb.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    bb7_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/bb7.mp3'), autoplay=False)

    bb7_row = Row([ft.Text('Bb7'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: bb7_audio.play()),],)

    bb7_modal = ft.AlertDialog(
        modal=True,
        title=bb7_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/bb7.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    bbm7_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/bbm7.mp3'), autoplay=False)

    bbm7_row = Row([ft.Text('Bbm7'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: bbm7_audio.play()),],)

    bbm7_modal = ft.AlertDialog(
        modal=True,
        title=bbm7_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/bbm7.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    bm7_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/bm7.mp3'), autoplay=False)

    bm7_row = Row([ft.Text('Bm7'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: bm7_audio.play()),],)

    bm7_modal = ft.AlertDialog(
        modal=True,
        title=bm7_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/bm7.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    bo7_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/bo7.mp3'), autoplay=False)

    bo7_row = Row([ft.Text('Bo7'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: bo7_audio.play()),],)

    bo7_modal = ft.AlertDialog(
        modal=True,
        title=bo7_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/bo7.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    c_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/c.mp3'), autoplay=False)

    c_row = Row([ft.Text('C'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: c_audio.play()),],)

    c_modal = ft.AlertDialog(
        modal=True,
        title=c_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/c.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    c6_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/c6.mp3'), autoplay=False)

    c6_row = Row([ft.Text('C6'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: c6_audio.play()),],)

    c6_modal = ft.AlertDialog(
        modal=True,
        title=c6_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/c6.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    c7_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/c7.mp3'), autoplay=False)

    c7_row = Row([ft.Text('C7'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: c7_audio.play()),],)

    c7_modal = ft.AlertDialog(
        modal=True,
        title=c7_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/c7.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    cm7_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/cm7.mp3'), autoplay=False)

    cm7_row = Row([ft.Text('Cm7'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: cm7_audio.play()),],)

    cm7_modal = ft.AlertDialog(
        modal=True,
        title=cm7_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/cm7.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    d7_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/d7.mp3'), autoplay=False)

    d7_row = Row([ft.Text('D7'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: d7_audio.play()),],)

    d7_modal = ft.AlertDialog(
        modal=True,
        title=d7_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/d7.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    d7b7_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/d7b7.mp3'), autoplay=False)

    d7b7_row = Row([ft.Text('D7b7'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: d7b7_audio.play()),],)

    d7b7_modal = ft.AlertDialog(
        modal=True,
        title=d7b7_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/d7b7.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    db_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/db.mp3'), autoplay=False)

    db_row = Row([ft.Text('Db'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: db_audio.play()),],)

    db_modal = ft.AlertDialog(
        modal=True,
        title=db_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/db.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    db7_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/db7.mp3'), autoplay=False)

    db7_row = Row([ft.Text('Db7'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: db7_audio.play()),],)

    db7_modal = ft.AlertDialog(
        modal=True,
        title=db7_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/db7.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    dm7_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/dm7.mp3'), autoplay=False)

    dm7_row = Row([ft.Text('Dm7'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: dm7_audio.play()),],)

    dm7_modal = ft.AlertDialog(
        modal=True,
        title=dm7_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/dm7.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    e7_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/e7.mp3'), autoplay=False)

    e7_row = Row([ft.Text('E7'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: e7_audio.play()),],)

    e7_modal = ft.AlertDialog(
        modal=True,
        title=e7_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/e7.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    eb_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/eb.mp3'), autoplay=False)

    eb_row = Row([ft.Text('Eb'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: eb_audio.play()),],)

    eb_modal = ft.AlertDialog(
        modal=True,
        title=eb_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/eb.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    eb7_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/eb7.mp3'), autoplay=False)

    eb7_row = Row([ft.Text('Eb7'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: eb7_audio.play()),],)

    eb7_modal = ft.AlertDialog(
        modal=True,
        title=eb7_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/eb7.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    ebm7_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/ebm7.mp3'), autoplay=False)

    ebm7_row = Row([ft.Text('Ebm7'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: ebm7_audio.play()),],)

    ebm7_modal = ft.AlertDialog(
        modal=True,
        title=ebm7_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/ebm7.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    em7_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/em7.mp3'), autoplay=False)

    em7_row = Row([ft.Text('Em7'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: em7_audio.play()),],)

    em7_modal = ft.AlertDialog(
        modal=True,
        title=em7_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/em7.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    eo7_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/eo7.mp3'), autoplay=False)

    eo7_row = Row([ft.Text('Eo7'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: eo7_audio.play()),],)

    eo7_modal = ft.AlertDialog(
        modal=True,
        title=eo7_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/eo7.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    f_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/f.mp3'), autoplay=False)

    f_row = Row([ft.Text('F'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: f_audio.play()),],)

    f_modal = ft.AlertDialog(
        modal=True,
        title=f_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/f.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    f6_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/f6.mp3'), autoplay=False)

    f6_row = Row([ft.Text('F6'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: f6_audio.play()),],)

    f6_modal = ft.AlertDialog(
        modal=True,
        title=f6_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/f6.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    f7_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/f7.mp3'), autoplay=False)

    f7_row = Row([ft.Text('F7'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: f7_audio.play()),],)

    f7_modal = ft.AlertDialog(
        modal=True,
        title=f7_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/f7.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    fm7_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/fm7.mp3'), autoplay=False)

    fm7_row = Row([ft.Text('Fm7'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: fm7_audio.play()),],)

    fm7_modal = ft.AlertDialog(
        modal=True,
        title=fm7_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/fm7.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    g_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/g.mp3'), autoplay=False)

    g_row = Row([ft.Text('G'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: g_audio.play()),],)

    g_modal = ft.AlertDialog(
        modal=True,
        title=g_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/g.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    g6_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/g6.mp3'), autoplay=False)

    g6_row = Row([ft.Text('G6'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: g6_audio.play()),],)

    g6_modal = ft.AlertDialog(
        modal=True,
        title=g6_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/g6.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    g7_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/g7.mp3'), autoplay=False)

    g7_row = Row([ft.Text('G7'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: g7_audio.play()),],)

    g7_modal = ft.AlertDialog(
        modal=True,
        title=g7_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/g7.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    g7b7_audio = ft.Audio(src=os.path.join(os.path.abspath(os.curdir),'assets/g7b7.mp3'), autoplay=False)

    g7b7_row = Row([ft.Text('G7b7'), ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, on_click=lambda _: g7b7_audio.play()),],)

    g7b7_modal = ft.AlertDialog(
        modal=True,
        title=g7b7_row,
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/g7b7.png'),
            width = 700,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Error!!!"),
        content=ft.Text("You should first pick an image"),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    pick_file_dialog = ft.FilePicker(on_result=pick_file_result)
    pick_file_path = ft.Text()
    # chord = ft.Text()

    start_button = ElevatedButton(text="Start", on_click=start_click,visible=True,width=150)

    set_button = ElevatedButton(text="Setting", on_click=set_click,visible=True,width=150)

    help_button = ElevatedButton(text="Help", on_click=help_click,visible=True,width=150)

    file_button = ElevatedButton(
                    "Pick File",
                    icon=icons.SAVE,
                    on_click=lambda _: pick_file_dialog.save_file(),
                    disabled=page.web,
                    visible=False,
                    width=150
                )
    
    photo_button = ElevatedButton(
                    "Take a Photo",
                    on_click=photo_click,
                    visible=False,
                    width=150
                )

    back_button = ElevatedButton(text="Back to Menu", on_click=back_click,visible=False,width=150)
    
    rec_button = ElevatedButton(text="Recognize", on_click=rec_click,visible=False,width=150)

    pr = ft.ProgressRing(visible=False)

    lv = ft.ListView(expand=1,visible=False, first_item_prototype=True)

    c1 = ft.Container(content=lv,visible=False,width=1000,height=200)

    help1 = ft.Text("How to Use This App", style=ft.TextThemeStyle.HEADLINE_SMALL, visible=False, weight=ft.FontWeight.BOLD)

    help2 = ft.Text("1) This App is developed to help guitar beginers to recognize chords, so the program ignores the components with less than three notes.", 
    style=ft.TextThemeStyle.BODY_LARGE,visible=False)

    help3 = ft.Text("2) This App accepts a line of score as input, analyzes and predicts the components with more than three notes and outputs its possible chords.", 
    style=ft.TextThemeStyle.BODY_LARGE,visible=False)

    help31 = ft.TextButton(text="Sample Input", visible=False, on_click=sample_click)

    help35 = ft.AlertDialog(
        modal=True,
        title=ft.Text("Sample Input"),
        content=Image(
            src=os.path.join(os.path.abspath(os.curdir),'test/test1.png'),
            width = 1000,
            fit='fitWidth',
            visible=True,
        ),
        actions=[
            ft.TextButton("OK", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    help4 = ft.Text("3) Due to the large number of chords, this App uses shell voicings to simplify chord prediction. Please refer to the website for details:", 
    style=ft.TextThemeStyle.BODY_LARGE,visible=False)

    help5 = ft.TextButton(text="Shell Voicings", visible=False, on_click=shell_click)

    help6 = ft.Text("4) But even with shell voicings, the number of chords is still hard to count, so the App chooses following 36 common chords to predict:", 
    style=ft.TextThemeStyle.BODY_LARGE,visible=False)

    help7 = ft.PopupMenuButton(
        items=[
            ft.PopupMenuItem(text="A7, A7#5, Ab, Ab7, Am7, Ao7"),
            ft.PopupMenuItem(text="B7, Bb, Bb7, Bbm7, Bm7, Bo7"),
            ft.PopupMenuItem(text="C, C6, C7, Cm7"),
            ft.PopupMenuItem(text="D7, D7b7, Db, Db7, Dm7"),
            ft.PopupMenuItem(text="E7, Eb, Eb7, Ebm7, Em7, Eo7"),
            ft.PopupMenuItem(text="F, F6, F7, Fm7"),
            ft.PopupMenuItem(text="G, G6, G7, Gm7, G7b7"),
        ]
    ,visible=False)

    help8 = ft.Text("5) This App introduces ambiguity to improve accuracy further, means that if it fails to reach a certain degree of confidence, this App doesn't output a single outcome, but four possible outcomes sorted in order of probability.", 
    style=ft.TextThemeStyle.BODY_LARGE,visible=False)

    help9 = ft.Text("6) Users can mannualy set the parameters of ambiguity in setting including the threshold(percent of ambiguity in results) and the number of backup chords.", 
    style=ft.TextThemeStyle.BODY_LARGE,visible=False)

    help10 = ft.Text("7) This App provides two modes to use first one is for e-score, another one is for camera-based photos including.", 
    style=ft.TextThemeStyle.BODY_LARGE,visible=False)

    help11 = ft.Text("8) When using the camera, please press space to take a photo, and Esc to exit.", 
    style=ft.TextThemeStyle.BODY_LARGE,visible=False)

    set1 = ft.Text("Please choose the percentage of ambiguity here:", visible=False, style=ft.TextThemeStyle.BODY_LARGE, weight=ft.FontWeight.BOLD)

    set2 = ft.Slider(min=0, max=30, divisions=6, value=30, label="{value}%", on_change=slider_changed, visible=False)

    set3 = ft.Text("There will be 30.0% ambiguity results",visible=False)

    set4 = ft.Text("\n\n\nPlease choose the mode here:", visible=False, style=ft.TextThemeStyle.BODY_LARGE, weight=ft.FontWeight.BOLD)

    set5 = ft.RadioGroup(content=ft.Column([
        ft.Radio(value="normal", label="E-score"),
        ft.Radio(value="tough", label="Photos")]),visible=False,value="normal")

    set6 = ft.Text("\n\n\nPlease choose the theme here:", visible=False, style=ft.TextThemeStyle.BODY_LARGE, weight=ft.FontWeight.BOLD)

    set7 = ft.Switch(label="Light theme", on_change=theme_changed,visible=False)

    page.overlay.extend([pick_file_dialog])

    myimg = Image(
            src=os.path.join(os.path.abspath(os.curdir),'assets/title2.png'),
            width = 650,
            height = 350,
            fit='fitWidth',
            visible=True,
    )

    a = ft.Container(ft.Column([Row(
            [
                set1,
                set2,
            ],
        ),

        set3,

        set4,

        set5,

        set6,

        set7,

        help1,

        help2,

        Row(
            [
                help3,
                help31, 
            ],
        ),

        Row(
            [
                help4,
                help5, 
            ],
        ),

        Row(
            [
                help6,
                help7, 
            ],
        ),  

        help8, 

        help9, 

        help10, 

        help11,  

        Row(
            [
                myimg,
            ],
            alignment="center",
        ),

        Row(
            [
                pr,
            ],
            alignment="center",
        ),

        Row(
            [
                im_404,
            ],
            alignment="center",
        ),

        Row(
            [
                c1,
            ],
        ),

        Row(
            [
                start_button,
            ],
            alignment="center",
        ),

        Row(
            [
                set_button,
            ],
            alignment="center",
        ),

        Row(
            [
                help_button,
            ],
            alignment="center",
        ),

        Row(
            [
                file_button,
                photo_button,
            ],
            alignment="center",
        ),

        Row(
            [
                rec_button,
            ],
            alignment="center",
        ),

        Row(
            [
                back_button,
            ],
            alignment="center",
        ),

        gm7_audio,

        a7_audio,

        am7_audio,

        ab7_audio,

        a75_audio,

        ab_audio,

        ao7_audio,

        b7_audio,

        bb_audio,

        bb7_audio,

        bbm7_audio,

        bm7_audio,

        bo7_audio,

        c_audio,

        c6_audio,

        c7_audio,

        cm7_audio,

        d7_audio,

        d7b7_audio,

        db_audio,

        db7_audio,

        dm7_audio,

        e7_audio,

        eb_audio,

        eb7_audio,

        ebm7_audio,

        em7_audio,

        eo7_audio,

        f_audio,

        f6_audio,

        f7_audio,

        fm7_audio,

        g_audio,

        g6_audio,

        g7_audio,

        g7b7_audio,])
        ,padding=20)


    st = ft.Stack(
        [
            b,
            a,
        ]
    )
    page.add(st)


    page.add(

        

        # chord,
    )

ft.app(target=main)