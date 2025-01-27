const animateService = (serviceId) =>{
    // get elements
    const service = document.getElementById('service'+serviceId);
    const serviceDescription = document.getElementById('description'+serviceId)
    const header = document.getElementById('header'+serviceId);


    // change style
    service.style.backgroundColor = 'white';
    serviceDescription.classList.remove('hide')
    header.style.color = 'black'
    header.style.fontSize = 'x-large'
    
}

const hideService = (serviceId)=>{
    try {
        // get elements

        const service = document.getElementById('service'+serviceId);
        const serviceDescription = document.getElementById('description'+serviceId)
        const header = document.getElementById('header'+serviceId);

            // change style
    service.style.backgroundColor = 'black';
    serviceDescription.classList.add('hide')
    header.style.color = 'white'
    header.style.fontSize = '1vh'        
    } catch (error) {
        
    }

}

const animateInnerLink = (serviceId) =>{
    // get elements
    const service = document.getElementById('inner'+serviceId);
    const serviceDescription = document.getElementById('innerDescription'+serviceId)
    const header = document.getElementById('innerHeader'+serviceId);


    // change style
    service.style.backgroundColor = 'white';
    serviceDescription.classList.remove('hide')
    header.style.color = 'black'
    header.style.fontSize = 'x-large'
    
}

const hideInnerLink = (serviceId)=>{
    try {
        // get elements

        const service = document.getElementById('inner'+serviceId);
        const serviceDescription = document.getElementById('innerDescription'+serviceId)
        const header = document.getElementById('innerHeader'+serviceId);

            // change style
    service.style.backgroundColor = 'black';
    serviceDescription.classList.add('hide')
    header.style.color = 'white'
    header.style.fontSize = '1vh'        
    } catch (error) {}
}


// wait till window loads
window.onload = function(){
    // get body. Currently has opacity set to zero. Increases to 1 over 3 seconds when the show class is added to it
    const body =  document.getElementById('body')
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