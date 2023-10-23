//E-MailJS Logic

document.getElementById("contact-form").addEventListener("submit", (event) => {

    event.preventDefault();/*will stop the tag form, from trying to send info over the network, which its default behaviour*/

    /* emailjs.sendForm(serviceID, templateID, templateParams, publicKey); */
    emailjs.sendForm("service_17xvqjl", "template_v96otqf", event.target).then(
        function () {

            Swal.fire({
                icon: 'success',
                title: 'well done,',
                text: 'thank you for submitting your Message',
            }) /* if the Message is sendt, it give a message*/

            confetti({
                particleCount: 400,
                spread: 200,
                shape:['circle','star','square']
            });

            document.getElementById("contact-form").reset();/* after sending the Message, the Form resets*/
        },

        function (error) {
            console.log(error)
            Swal.fire({
                icon: 'error',
                title: '404',
                text: 'Contact Administration',
            });
        },
    );
})
