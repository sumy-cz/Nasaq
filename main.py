from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
TOKEN = "8766527245:AAFYzV6zhyPKmJz7tngY9APpOyuPvDD9Huk"
#نسق | مكتبة العلوم التطبيقية 
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    main_keyboard = [
        ["اللغة العربية 1 | AR011", "اللغة الإنجليزية 1 | EL011"],
        ["رياضة 1 | MA011", "الاحصاء العام | ST011"],
        ["طبيعة 2 | PH011"],
        ["عودة للخلف"] 
    reply_markup = ReplyKeyboardMarkup(main_keyboard, resize_keyboard=True)
    await update.message.reply_text("أهلًا بك في بوت مرحلة العلوم التطبيقية! اختر المادة المطلوبة:", reply_markup=reply_markup)
# 2.المواد الدراسية 
async def show_course_menu(update: Update, course_code: str):
    course_keyboard = [
        [f"مقرر النصفي والنهائي | {course_code}"],
        [f"Midterm | {course_code}", f"Final | {course_code}"],
        [f"كتب ومراجع | {course_code}"],
        [f"كوزات القناة | {course_code}"],
        ["Go Back"]
    ]
    reply_markup = ReplyKeyboardMarkup(course_keyboard, resize_keyboard=True)
    await update.message.reply_text(f"اختر المحتوى المطلوب لمادة {course_code}:", reply_markup=reply_markup)
# 3. 
async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    # زر الرجوع للقائمة الرئيسية
    if text == "عودة للقائمة الاساسية" or text == "Main Menu":
        await start(update, context)
        return

    # 
    if "MA011" in text and "مقرر" not in text and " كتب" not in text:
        await show_course_menu(update, "MA011")
    elif "PH011" in text and "مقرر" not in text and " كتب" not in text:
        await show_course_menu(update, "PH011")
    elif "AR011" in text:
        await show_course_menu(update, "AR011")
    elif "EL011" in text:
        await show_course_menu(update, "EL011")
    elif "ST011" in text:
        await show_course_menu(update, "ST011")

    # الردود عند اختيار المحتوى الداخلي للمادة (مثال: رياضة 1 MA011)
    elif text == "مقرر النصفي والنهائي | MA011":
        msg = (
"نسق | علوم تطبيقية\n"
            " - رياضة 1 || MA011.\n\n"
            "- مقرر النصفي\n"
            "- ملخص للنصفي\n"
            "- مقرر النهائي...\n\n"
            "🔗 [اضغط هنا لعرض كافة الرسائل وال)"
        )
        await update.message.reply_text(msg, parse_mode='Markdown')

    # الردود عند اختيار المحتوى الداخلي للمادة (مثال: طبيعة 2 PH011)
    elif text == "مقرر النصفي والنهائي | PH011":
        msg = (
            "تعلم | علوم تطبيقية\n"
            "📍 - طبيعة 2 || PH011.\n\n"
            "- مقرر النصفي\n"
            "- مقرر النهائي\n"
            "- قناة د. خالد التميمي\n"
            "- ملخص لقوانين النصفي باستخدام المخططات...\n\n"
            "🔗 [اضغط هنا لعرض كافة الرسائل والملفات](https://t.me/https://t.me/Nasaq_edu)"
        )
        await update.message.reply_text(msg, parse_mode='Markdown')

def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_messages))
    
    print("البوت يعمل بنجاح...")
    app.run_polling()

if __name__ == '__main__':
    main()
