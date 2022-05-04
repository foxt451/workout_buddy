import {
    ChatUI
} from "./ui.js";
import {
    ChatSession
} from "./chat.js";

import {
    initializeApp
} from "https://www.gstatic.com/firebasejs/9.6.10/firebase-app.js";
import * as fs
from "https://www.gstatic.com/firebasejs/9.6.10/firebase-firestore.js";

const firebaseConfig = {

    apiKey: "AIzaSyBlCF1MRhwG7JHA9-SuSUQLiaQXCqPj9rM",
    authDomain: "workoutbuddy-70091.firebaseapp.com",
    projectId: "workoutbuddy-70091",
    storageBucket: "workoutbuddy-70091.appspot.com",
    messagingSenderId: "102463363442",
    appId: "1:102463363442:web:16d6528bb454b17259a5eb"
};


// Initialize Firebase
const app = initializeApp(firebaseConfig);
const db = fs.getFirestore(app);

const userFrom = JSON.parse(document.getElementById('user-from').textContent).id;
const userTo = JSON.parse(document.getElementById('user-to').textContent).id;

const userFromName = JSON.parse(document.getElementById('user-from').textContent).username;
const userToName = JSON.parse(document.getElementById('user-to').textContent).username;

const userFromLink = JSON.parse(document.getElementById('user-from').textContent).userlink;
const userToLink = JSON.parse(document.getElementById('user-to').textContent).userlink;
console.log(userToLink);

const sess = new ChatSession(db, userFrom, userTo);

const chatList = document.querySelector('.chat-list');
const newChatForm = document.querySelector('.new-chat');

newChatForm.addEventListener('submit', e => {
    e.preventDefault();
    const message = newChatForm.message.value.trim();
    sess.sendMessage(message).then(
        () => {
            newChatForm.reset();
        }
    ).catch(
        err => {
            console.log(err);
        }
    );
});

const chatUI = new ChatUI(chatList);

const setListener = () => sess.getMessages(doc => {
    // here doc.userFrom means who sent the message (can be both users)
    // and userFrom means current user (request.user) (who will pose as a sender if they click 'Send')
    chatUI.addMessage(doc, ...(doc.userFrom === userFrom ? [userFromName, userFromLink] : [userToName, userToLink]));
});
setListener();