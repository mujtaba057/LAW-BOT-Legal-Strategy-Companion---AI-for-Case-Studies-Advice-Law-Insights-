css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #00cccc
}
.chat-message.bot {
    background-color: #ff0066
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/nM74bMt/sofia.jpg">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''
user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://i.ibb.co/gPbfjHG/human.jpg">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
# css = '''
# <style>
# .chat-message {
#     padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
# }
# .chat-message.user {
#     background-color: #4eb5f1
# }
# .chat-message.bot {
#     background-color: #475063
# }
# .chat-message .avatar {
#   width: 20%;
# }
# .chat-message .avatar img {
#   max-width: 78px;
#   max-height: 78px;
#   border-radius: 50%;
#   object-fit: cover;
# }
# .chat-message .message {
#   width: 80%;
#   padding: 0 1.5rem;
#   color: #fff;
# }
# '''

# bot_template = '''
# <div class="chat-message bot">
#     <div class="avatar">
#         <img src="https://i.ibb.co/9H2Fgr0/Screenshot-2023-10-18-145545.gif">
#     </div>
#     <div class="message">{{MSG}}</div>
# </div>
# '''

# user_template = '''
# <div class="chat-message user">
#     <div class="avatar">
#         <img src="https://i.ibb.co/rdZC7LZ/Photo-logo-1.png">
#     </div>    
#     <div class="message">{{MSG}}</div>
# </div>
# '''