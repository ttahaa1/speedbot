const { Telegraf } = require('telegraf');
const bot = new Telegraf('YOUR_BOT_TOKEN');

// استمع للرسائل النصية وقم بتنفيذ الإجراء المناسب
bot.on('text', (ctx) => {
  const command = ctx.message.text;
  // قم بتنفيذ الإجراء المناسب استنادًا إلى الأمر المستلم
  executeCommand(command, ctx);
});

// وظيفة لتنفيذ الأوامر
function executeCommand(command, ctx) {
  // قم بتنفيذ الأمر المناسب هنا
  // مثال:
  if (command === '/start') {
    ctx.reply('مرحبًا بك! يمكنك بدء استخدام البوت الخاص بك.');
  } else if (command === '/info') {
    ctx.reply('معلومات عن البوت...');
  } else {
    ctx.reply('لم يتم فهم الأمر.');
  }
}

// تشغيل البوت
bot.launch();
