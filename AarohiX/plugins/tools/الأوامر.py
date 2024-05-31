
import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import InlineKeyboardButton, CallbackQuery, InlineKeyboardMarkup, Message
from typing import Union
from pyrogram.types import InlineKeyboardButton
from AronoX import app
from AronoX.misc import HAPP, SUDOERS, XCB
from config import OWNER_ID
                                       
                                       
@app.on_callback_query(filters.regex("zzzback"))
async def zzzback(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""<b>» مرحبًــا بك عـزيـزي</b>\n<b>» استخـدم الأزرار بالاسفـل\n» لـ تصفـح أوامـر بوت فهـد 🇵🇸</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "〔 أوامـــر التشغيــل 〕", callback_data="zzzll"),
                ],[
                    InlineKeyboardButton(
                        "〔 أوامـــر القنـاة 〕", callback_data="zzzch"),
                    InlineKeyboardButton(
                        "〔 أوامـــر الادمـن 〕", callback_data="zzzad"),
                ],[
                    InlineKeyboardButton(
                        "〔 أوامـــر المطــور 〕", callback_data="zzzdv"),
                ],[
                    InlineKeyboardButton(
                        "「  مبـرمج السـورس 」 ", url="https://t.me/PPF22"),
                ],
            ]
        ),
    )



@app.on_callback_query(filters.regex("zzzdv") & SUDOERS)
async def mpdtsf(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""<b>» مرحبًــا بك عـزيـزي المطـور </b>\n\n<b>» استخـدم الأزرار بالاسفـل\n» لـ تصفـح أوامـر بوت فهـد</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "〔 التحـديث 〕", callback_data="zzzup"),
                ],[
                    InlineKeyboardButton(
                        "〔 الـرفــع 〕", callback_data="zzzsu"),
                    InlineKeyboardButton(
                        "〔 الـحظــر 〕", callback_data="zzzbn"),
                ],[
                    InlineKeyboardButton(
                        "〔 الإشعــارات والمُساعـد 〕", callback_data="zzzas"),
                ],[
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzback"),
                ],
            ]
        ),
    )



@app.on_callback_query(filters.regex("zzzll"))
async def zzzll(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
<b>⎉︙قائمــة أوامـــر الـتشغـيـل :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
تشغيل + (اسم الأنشودة/ اسم السورة / رابط الاغنية)
<b>- لــ تـشـغـيل  أنشـودة/ ســورة فـي الـمكـالـمـة الـصـوتـيـة</b>

فيديو + (اسم المقـطـع / رابط المقـطـع)
<b>- لــ تـشـغـيل فيـديـو فـي الـمكـالـمـة المـرئيـة</b>

بحث + الاسـم
<b>- لـ تحميـل الأناشيـد أو القرآن الكريـم والمقـاطـع الصـوتيــة مـن اليوتيـوب</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzad"))
async def zzzad(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
<b>⎉︙قائمــة أوامـــر الادمــن :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆

الاعدادات
<b>- لـ عـرض إعـدادات اوضـاع التشغيـل</b>

ايقاف / انهاء / قف
<b>- لـ إيقـاف تـشغـيـل الـمـوسـيـقـى فـي المكـالمـة</b>

ق / اسكت
<b>- لـ إيقـاف تشغيـل الموسيـقـى فـي المكالمـة مـؤقتـاً</b>

كمل / ك
<b>- لـ اسـتـئـنـاف تـشغـيـل الـمـوسـيـقـى فـي المكـالمـة</b>

تخطي / سكيب
<b>- لـ تخطـي الاغنيـة وتشغيـل الاغنيـة التاليـه</b>

الاغاني
<b>- لـ معـرفـة الاغـانـي المـوجـودة فـي قائمـة الانتظـار</b>

بنج
<b>- لـ عـرض سـرعـة تشغيـل البـوت</b>

رفع ادمن/تنزيل ادمن
<b>- لـ رفـع/تنزيـل ادمـن فـي البـوت</b>

الادمنية
<b>- لـ عـرض قائمـة أدمنيـة البـوت</b>
""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzch"))
async def zzzch(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
<b>⎉︙قائمــة أوامـــر التشغيــل فـي القنــاة :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- ارفـع البـوت إشـراف في القنـاة و شغـل مباشـر</b>
<b>- أرسـل (ربط) + يـوزر القنـاة لـ الربـط</b>
<b>- ثم استخـدم الأوامـــر بالاسفـل لـ التشغيـل</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
تشغيل / ش + اسم الأنشودة/ اسم السورة
<b>- لــ تـشـغـيل  أنشـودة/ ســورة فـي الـمكـالـمـة الـصـوتـيـة</b>

فيديو + اسم المقـطـع
<b>- لــ تـشـغـيل فيـديـو فـي الـمكـالـمـة المـرئيـة</b>

ايقاف / اخرص / اسكت
<b>- لـ إيقـاف تـشغـيـل الـمـوسـيـقـى فـي المكـالمـة</b>

مؤقت / ق
<b>- لـ إيقـاف تشغيـل الموسيـقـى فـي المكالمـة مـؤقتـاً</b>

كمل / استئناف / ك
<b>- لـ اسـتـئـنـاف تـشغـيـل الـمـوسـيـقـى فـي المكـالمـة</b>

تخطي / سكيب
<b>- لـ تخطـي الاغنيـة وتشغيـل الاغنيـة التاليـه</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
تقديم + عـدد الثـوانـي
<b>- لـ تقديـم الأنشـودة/السورة لـ الامـام</b>
رجوع + عـدد الثـوانـي
<b>- لـ إرجـاع الأنشـودة/السورة لـ الخـلف</b>
""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzup") & SUDOERS)
async def zzzup(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
<b>⎉︙قائمــة أوامـــر المطــور :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- قائمــة أوامـــر التحـديثـات :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆

السجلات
<b>- لـ إحضار سجـلات البـوت 📋</b>

تحديث
<b>- لـ تحديـث البــوت</b>

اعادة تشغيل
<b>- لـ اعـادة تشغيـل البــوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzdv"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzsu") & SUDOERS)
async def zzzsu(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
<b>⎉︙قائمــة أوامـــر المطــور :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- قائمــة أوامـــر الـرفــع :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆

رفع مطور/تنزيل مطور
<b>- لـ رفـع/تنزيـل شخـص مطـور فـي البـوت</b>

المطورين
<b>- لـ عـرض قائمـة مطـورين البـوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzdv"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzbn") & SUDOERS)
async def zzzbn(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
<b>⎉︙قائمــة أوامـــر المطــور :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- قائمــة أوامـــر الحظــر :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆

احظره عام/الغاء الحظر العام
<b>- لـ حظـر/إلغـاء حظـر شخـص من استخـدام البـوت عـام</b>

المحظورين عام
<b>- لـ جلب قائمـة المحظـورين عـام فـي البـوت</b>

حظر مجموعة
<b>- لـ حظـر/إلغـاء حظـر مجموعـة من استخـدام البـوت</b>

المجموعات المحظورة
<b>- لـ جلب قائمـة بالمجمـوعـات المحظـورة مـن استـخـدام البـوت</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzdv"),
               ],
          ]
        ),
    )


@app.on_callback_query(filters.regex("zzzas") & SUDOERS)
async def zzzas(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
<b>⎉︙قائمــة أوامـــر المطــور :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<b>- قائمــة أوامـــر المســاعــد ✅ :</b>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆

السجل [ تفعيل / تعطيل ]
<b>- لـ تفعيـل/تعطيـل إشعـارات مجموعـة سجـل البــوت</b>

غادر
<b>لـ مُغادرة البوت المجموعـة عند يأمره المطــور</b>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجـوع", callback_data="zzzdv"),
               ],
          ]
        ),
    )
    
    #حقوق_زلزال_الهيبة
