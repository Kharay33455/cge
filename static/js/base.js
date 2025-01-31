// origin
const origin = window.location['origin']

// animate service show on click provided it isnt being shown.
const animateService = (serviceId) => {
    // get elements
    const service = document.getElementById('service' + serviceId);
    const serviceDescription = document.getElementById('description' + serviceId)
    const header = document.getElementById('header' + serviceId);


    // change style
    service.style.backgroundColor = 'white';
    serviceDescription.classList.remove('hide')
    header.style.color = 'black'
    header.style.fontSize = 'x-large'

}
// Hide service text
const hideService = (serviceId) => {
    try {
        // get elements

        const service = document.getElementById('service' + serviceId);
        const serviceDescription = document.getElementById('description' + serviceId)
        const header = document.getElementById('header' + serviceId);

        // change style
        service.style.backgroundColor = 'black';
        serviceDescription.classList.add('hide')
        header.style.color = 'white'
        header.style.fontSize = '1vh'
    } catch (error) {

    }

}

// animate inner link
const animateInnerLink = (serviceId) => {
    // get elements
    const service = document.getElementById('inner' + serviceId);
    const serviceDescription = document.getElementById('innerDescription' + serviceId)
    const header = document.getElementById('innerHeader' + serviceId);


    // change style
    service.style.backgroundColor = 'white';
    serviceDescription.classList.remove('hide')
    header.style.color = 'black'
    header.style.fontSize = 'x-large'

}

const hideInnerLink = (serviceId) => {
    try {
        // get elements

        const service = document.getElementById('inner' + serviceId);
        const serviceDescription = document.getElementById('innerDescription' + serviceId)
        const header = document.getElementById('innerHeader' + serviceId);

        // change style
        service.style.backgroundColor = 'black';
        serviceDescription.classList.add('hide')
        header.style.color = 'white'
        header.style.fontSize = '1vh'
    } catch (error) { }
}

// animate chat on hover
const animateChatWrapper = (style) => {

    const chat = document.getElementById('chatIcon');
    if (style === 'expand') {
        chat.style.width = '4vb'
        chat.style.height = '4vb'
    }
    else if (style === 'shrink') {
        chat.style.width = '2vb'
        chat.style.height = '2vb'
    }
}

// animate chat box
const animateChatBox = (type) => {
    const chatBox = document.getElementById('chatBox')
    if (type === 'show') {
        chatBox.style.opacity = '1';
        chatBox.style.top = '0';
        chatBox.style.left = '0';
        chatBox.classList.add('animateChatBox');
        setTimeout(() => {
            chatBox.classList.remove('animateChatBox')
        }, 1000);
    }
    if (type === 'hide') {
        chatBox.style.opacity = '0';
        chatBox.style.top = '100vh';
        chatBox.style.left = '100vw'
            ; chatBox.classList.add('closeChatBox');
        setTimeout(() => {
            chatBox.classList.remove('closeChatBox')
        }, 1000);
    }
}

// create new message 
const drawMessage = (item, messageBox) => {
    console.log('here')
    // create parent div and style messag according to user or support
    const parent = document.createElement('div');
    parent.classList = 'message ' + (item['fromSupport'] ? 'supportMessage' : 'userMessage');
    // create blank div
    const blank = document.createElement('div');
    // append blank div only if user is the message sender
    !item['fromSupport'] && parent.appendChild(blank);

    // create message and time div
    const mat = document.createElement('div');
    mat.classList = 'messageAndTime ' + (item['fromSupport'] ? 'supportMat' : 'userMat');

    // create image if it ecists
    if (item['image']) {
        const image = document.createElement('img');
        image.src = item['image'];
        image.style.width = '100%'
        const imageDiv = document.createElement('div');
        imageDiv.appendChild(image);
        mat.appendChild(imageDiv);
    }

    // create and append text div if it's not none
    if (item['text']) {
        const messageText = document.createElement('span');
        messageText.classList = 'messageText'
        messageText.innerHTML = item['text'];
        // div to hold text
        const textDiv = document.createElement('div');
        textDiv.appendChild(messageText);
        mat.appendChild(textDiv);
    }

    // create time div and append
    const timeDiv = document.createElement('div');
    timeDiv.classList.add('timeWrapper');
    //time element

    const timeElement = document.createElement('span');
    timeElement.innerHTML = item['time'];
    timeElement.classList.add('time');
    timeDiv.appendChild(timeElement);
    mat.appendChild(timeDiv);
    parent.appendChild(mat);

    //append to message box last
    messageBox.appendChild(parent);

}

// fetch chat with AJAX
const fetchChat = async () => {
    try {
        const name = document.getElementById('name').value
        const email = document.getElementById('email').value
        const chatID = document.getElementById('chatID').value
        const csrf = document.getElementById('csrf').value
        const title = document.getElementById('title').value

        const response = await fetch(origin + '/chat',
            {
                method: 'POST',
                headers: {
                    'X-CSRFTOKEN': csrf
                },
                body: JSON.stringify({ 'name': name, 'email': email, 'chatID': chatID, 'title': title })
            }
        )
        const result = await response.json();
        if (result['status'] === 204) {
            const errMsg = document.getElementById('errMsg')
            errMsg.innerHTML = result['data'];
            setTimeout(() => {
                errMsg.innerHTML = '';
            }, 2000);
        }
        if (result['status'] === 200) {
            console.log('result is ', result)
            // show box
            const showDiv = document.getElementById('chatStarted')
            showDiv.style.opacity = '1';
            showDiv.style.zIndex = '1';
            const hideDiv = document.getElementById('startChat');
            hideDiv.style.opacity = '0';
            hideDiv.style.zIndex = '0';
            document.getElementById('messageDiv').style.opacity = '1';
            // get mesage box element
            const messageBox = document.getElementById('messages');
            // loop through messages
            result['data']['messages'].map((item) => {
                drawMessage(item, messageBox);
            });
            const scrollDiv = document.getElementById('scrollDiv');
            scrollDiv.scrollTop = scrollDiv.scrollHeight;
            document.getElementById('chatTitle').innerHTML = result['data']['title'];
            document.getElementById('id').value = result['data']['id'];
        }
    } catch (error) {
        console.error(error);
    }
}


// send new message
const newMessage = async () => {
    try {
        const image = document.getElementById('image').files[0];

        const text = document.getElementById('messageForm');

        const csrf = document.getElementById('csrf').value;

        const chatId = document.getElementById('id').value;

        const form = new FormData();

        form.append('text', text.value);

        if (image !== undefined && image instanceof File) {
            form.append('image', image);
        } else {
            form.append('image', null);
        }

        form.append('chatId', chatId);

        const response = await fetch(origin + '/chat/new-message', {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrf
            },
            body: form
        });

        const result = await response.json();
        if (result['status'] === 200) {
            const message = result['message'];
            const messageBox = document.getElementById('messages');
            drawMessage(message, messageBox);
            text.value = "";
            const _image = document.getElementById('image');
            _image.value = '';
            const scrollDiv = document.getElementById('scrollDiv');
            scrollDiv.scrollTop = scrollDiv.scrollHeight;
        }

    } catch (error) {
        console.log(error);
    }
}

// wait till window loads
window.onload = function () {
    // get body. Currently has opacity set to zero. Increases to 1 over 3 seconds when the show class is added to it
    const body = document.getElementById('body')
    // get the name header. Currently set to be invisible, comes into view after animation starts
    const nameHeader = document.getElementById('companyNameHeader');
    // verification tic
    const verified = document.getElementById('verified');

    // set final values
    body.style.display = 'block';
    nameHeader.style.paddingLeft = '20vw'
    nameHeader.style.fontSize = '5vw';
    verified.style.width = '10vw';
    verified.style.height = '10vw'
    verified.style.fill = '#1DA1F2'

    // load animations
    body.classList.add('show');
    nameHeader.classList.add('mover');
    verified.classList.add('animateVerified');


}