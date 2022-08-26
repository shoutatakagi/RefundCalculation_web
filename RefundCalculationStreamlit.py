import streamlit as st
import datetime
import math

st.title('返金額算出')
st.caption('Kredo Onlie Campの返金額を算出')

#各コースの料金
BC_Fee = 149400
DevS_Fee = 174300
DevA_Fee = 174300
DevE_Fee = 174300
DesS_Fee = 174300
DesA_Fee = 174300

StudentName = st.text_input('生徒氏名')
CXL_Date = st.date_input('キャンセル申し入れ日')
st.text(f'受講コースにチェックを入れてください')
English = st.checkbox('English')
IT = st.checkbox('IT')

#英語を受講する生徒の返金額算出
if English == True:
    English_Course_Start_Date = st.date_input("英語レッスンの開始日")
    English_Lesson_Fees = st.number_input("英語レッスン料金", value=0)
    English_Used_Points = st.number_input("英語の使用済みポイント", value=0)
    #英語のみを受講する生徒の返金額算出
    if IT == False:
        English_Refund_btn = st.button('返金額算出', key='English')
        if English_Refund_btn:
            EnglishRefund = English_Lesson_Fees - (10000 + English_Used_Points * 10)
            st.text(f'{StudentName}様への返金額は{EnglishRefund}円です')

#ITを受講する生徒の返金額算出
if IT == True:
    Before_Start_Class = st.radio("受講前受講後どちらでしょうか",('受講前', '受講後'), horizontal=True)
    #受講前
    if Before_Start_Class == '受講前':
        ChangeStartDay = st.radio("時期変更していますか？",('している', 'していない'), horizontal=True)
        IT_Lesson_Fees = st.number_input("ITレッスン料金", value=0)
        Fee_per_lesson = IT_Lesson_Fees / 130
        BeforeStartClass_Refund_btn = st.button('返金額算出', key='BeforeStart')
        if BeforeStartClass_Refund_btn:
            #ITのみを受講する生徒の返金額算出
            if English == False:
                #時期変更の有無による返金額算出
                if ChangeStartDay == 'していない':
                    BeforeStartClass_Refund = (IT_Lesson_Fees * 0.7) 
                else:
                    BeforeStartClass_Refund = (IT_Lesson_Fees * 0.6)
            #英語とITを受講する生徒の返金額算出
            else:
                #時期変更の有無による返金額算出
                if ChangeStartDay == 'していない':
                    BeforeStartClass_Refund = (IT_Lesson_Fees * 0.7) + (English_Lesson_Fees - English_Used_Points * 10)
                else:
                    BeforeStartClass_Refund = (IT_Lesson_Fees * 0.6) + (English_Lesson_Fees - English_Used_Points * 10)
            st.text(f'{StudentName}様への返金額は{BeforeStartClass_Refund}円です')
    #受講後
    else:
        ClassOrPersonal = st.radio("IT受講形式はクラスorパーソナル？",('クラス', 'パーソナル'), horizontal=True)
        IT_Course_Start_Date = st.date_input("ITレッスンの開始日")
        #パーソナル生徒への返金額算出
        if ClassOrPersonal == 'パーソナル':
            IT_Lesson_Fees = st.number_input("ITレッスン料金", value=0)
            Fee_per_lesson = IT_Lesson_Fees / 130
            Personal_Lessons_Taken = st.number_input("パーソナルの受講済みレッスン数", value=0)
            Personal_Refund_btn = st.button('返金額算出', key='Personal')
            if Personal_Refund_btn:
                #ITのみを受講する生徒の返金額算出
                if English == False:
                    if CXL_Date - IT_Course_Start_Date < datetime.timedelta(days = 28):
                        Personal_Refund = (IT_Lesson_Fees - Personal_Lessons_Taken * Fee_per_lesson ) * 7 / 10 
                    if datetime.timedelta(days = 28) <= CXL_Date - IT_Course_Start_Date < datetime.timedelta(days = 56):
                        Personal_Refund = (IT_Lesson_Fees - Personal_Lessons_Taken * Fee_per_lesson ) * 5 / 10 
                    if datetime.timedelta(days = 56) <= CXL_Date - IT_Course_Start_Date < datetime.timedelta(days = 84):
                        Personal_Refund = (IT_Lesson_Fees - Personal_Lessons_Taken * Fee_per_lesson ) * 3 / 10 
                    if datetime.timedelta(days = 84) <= CXL_Date - IT_Course_Start_Date < datetime.timedelta(days = 112):
                        Personal_Refund = (IT_Lesson_Fees - Personal_Lessons_Taken * Fee_per_lesson ) * 1 / 10 
                    if datetime.timedelta(days = 112) < CXL_Date - IT_Course_Start_Date:
                        Personal_Refund = 0
                #英語とITを受講する生徒の返金額算出
                else:
                    if CXL_Date - IT_Course_Start_Date < datetime.timedelta(days = 28):
                        Personal_Refund = (IT_Lesson_Fees - Personal_Lessons_Taken * Fee_per_lesson ) * 7 / 10 + (English_Lesson_Fees - English_Used_Points * 10)
                    if datetime.timedelta(days = 28) <= CXL_Date - IT_Course_Start_Date < datetime.timedelta(days = 56):
                        Personal_Refund = (IT_Lesson_Fees - Personal_Lessons_Taken * Fee_per_lesson ) * 5 / 10 + (English_Lesson_Fees - English_Used_Points * 10)
                    if datetime.timedelta(days = 56) <= CXL_Date - IT_Course_Start_Date < datetime.timedelta(days = 84):
                        Personal_Refund = (IT_Lesson_Fees - Personal_Lessons_Taken * Fee_per_lesson ) * 3 / 10 + (English_Lesson_Fees - English_Used_Points * 10)
                    if datetime.timedelta(days = 84) <= CXL_Date - IT_Course_Start_Date < datetime.timedelta(days = 112):
                        Personal_Refund = (IT_Lesson_Fees - Personal_Lessons_Taken * Fee_per_lesson ) * 1 / 10 + (English_Lesson_Fees - English_Used_Points * 10)
                    if datetime.timedelta(days = 112) < CXL_Date - IT_Course_Start_Date:
                        Personal_Refund = 0
                st.text(f'{StudentName}様への返金額は{Personal_Refund}円です')
        #クラス生徒への返金額算出
        else:
            ClassNotTaken = st.radio("未受講のコースを選択してください",('すべて受講済み', 'Dev(S)~(A)', 'Dev(A)~(E)', 'Dev(E)のみ', 'Des(S)~Des(A)', 'Des(A)のみ'), horizontal=True)
            Group_Refund_btn = st.button('返金額算出', key='Group')
            if Group_Refund_btn:
                #未受講のクラスから返金額を算出
                if ClassNotTaken == 'すべて受講済み':
                    Group_Refund = English_Lesson_Fees - English_Used_Points * 10
                if ClassNotTaken == 'Dev(S)~(E)':
                    Group_Refund = (DevS_Fee + DevA_Fee + DevE_Fee) * 5 / 10 + English_Lesson_Fees - English_Used_Points * 10
                if ClassNotTaken == 'Dev(A)~(E)':
                    Group_Refund = (DevA_Fee + DevE_Fee) * 5 / 10 + English_Lesson_Fees - English_Used_Points * 10
                if ClassNotTaken == 'Dev(E)':
                    Group_Refund = DevE_Fee * 5 / 10 + English_Lesson_Fees - English_Used_Points * 10
                if ClassNotTaken == 'Des(S)~(A)':
                    Group_Refund = (DesS_Fee + DesA_Fee) * 5 / 10 + English_Lesson_Fees - English_Used_Points * 10
                if ClassNotTaken == 'Des(A)':
                    Group_Refund = DesA_Fee * 5 / 10 + English_Lesson_Fees - English_Used_Points * 10
                st.text(f'{StudentName}様への返金額は{Group_Refund}円です')

    

