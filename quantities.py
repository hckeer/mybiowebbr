@import url('<link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap" rel="stylesheet');
* {
    margin:0;
    padding: 0;
    box-sizing: border-box;
    text-decoration: none;
    border: none;
    outline: none;
    scroll-behavior: smooth;
    font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
}

:root {
    --bg-color: #000000;
    --second-bg-color: #161616;
    --text-color: #fff;
    --main-color:#7b4bb7;
}


html {
    font-size: 62.5%;
    overflow-x: hidden;
}

body {
    background: var(--bg-color);
    font-family: "Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif";
    color: var(--text-color)
}

html::-webkit-scrollbar {
    width: 0.8rem;
}
html::-webkit-scrollbar-track{
    background: var(--bg-color);
}
html::-webkit-scrollbar-thumb {
    background: var(--main-color);
}


.header  {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    padding: 3rem 9%;
    background: rgba(0, 0, 0, 0.7);
    filter: drop-shadow(10px);
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 100;
}


.logo {
    font: 30rem;
    color: var(--main-color);
    font-weight: 500;
    cursor: pointer;
    transition: 0.5s;
    font-size:xx-large;
    box-shadow: #e13c26;
    border-radius: 10px;
}

.logo:hover{
    transform: scale(1.1);

}

.navbar a{
    font-size: 1.8rem;
    color: var(--text-color);
    margin-left: 4rem;
    font-weight: 500;
    transition: 0.3s ease;
    border-bottom: 3px solid transparent;
}   

.navbar:hover,
.navbar a.active {
    color: var(--main-color);
    border-bottom: 3px solid var(--main-color);

}

#menu-icon {
    font-size: 3.5rem;
    color: var(--main-color);
    display: none;
}


@media (max-width: 995px) {
    #menu-icon {
        display: block;
    }
    .navbar {
        position: absolute;
        top: 100%;
            right: 0;
        width: 40%;
        border-left: 3px solid var(--main-color);
        border-bottom: 3px solid var(--main-color);
        padding: 1rem 3%;
        background-color: var(--second-bg-color);
        border-top: 0.1rem solid rgba(0,0,0,0.1);
        display: none;
    }
    .navbar.active {
        display: block;
    }
    .navbar a{
        display: block;
        font-size: 2rem;
        margin: 3rem 0;
    }
    .navbar :hover,
    .navbar a.navbar {
        padding: 1rem;
        border-radius: 0.5rem;
        border-bottom: 0.5rem solid var(--main-color);
    }
    
}

    


section {
    min-height: 100px;
    padding: 5rem 9% 5rem;

}

.home {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 8rem;
    background: var(--bg-color);
}

.home .home-content h1{
    font-size: 6rem;
    font-weight: 700;
    line-height: 1.3;
}

span {
    color: var(--main-color);
}

.home-content h3 {
    font-size: 4rem;
    margin-bottom: 1rem;
    font-weight: 700;
}

.home-img img{
    position: relative;
    width: 32vw;
    border-radius: 50%;
    box-shadow: 0 0 25px var(--main-color);
}

.home-img img:hover{
    transform: scale(1.01);
    filter: drop-shadow(0 0 25px var(--main-color));
    transition: 1s;
}

.home-content p{
    font-size: 1.8rem;
    font-weight: 500;
}

.social-icon a{
    display: inline-flex;
    justify-content: center;
    align-items: center;
    width: 4rem;
    height: 4rem;
    background: transparent;
    border-radius: 50%;
    color: var(--main-color);
    margin: 3rem 1.5rem;
    transition: 0.5s;
}


.social-icon a:hover {
    color:black;
    transform: scale(1.3)translateY(-5px);
    background: var(--main-color);
    box-shadow: 0 0 25px var(--main-color);
}

.btn {
    display: inline-block;
    padding: 1rem 2.8rem;
    background: var(--bg-color);
    border-radius: 4rem;
    font-size: 1.6rem;
    color: var(--main-color);
    border: 2px solid var(--main-color);
    letter-spacing: 0.1rem;
    font-weight: 600;
    transition: 0.3s ease;
    cursor: pointer;
}

.btn:hover {
    transform: scale(1.03);
    background-color: black;
    color: var(--text-color);
    box-shadow: 0 0 25px;
}

.typing-text {
    font-size: 34px;
    font-weight: 600;
    min-width: 280px;
}
.typing-text span{
    position: relative;
}
.typing-text span::before{
    content: 'Software Developer';
    color: var(--main-color);
    animation: words 20s infinite;
}

.typing-text span::after{
    content: '';
    background: var(--bg-color);
    position: absolute;
    width: calc(100% + 8px);
    height: 100%;
    border-left: 3px solid var(--bg-color);
    right: -8;
    animation: cursor 0.6s infinite, typing 20s steps(14) infinite;
}



@keyframes cursor {
    to {
        border-left: 3px solid var(--main-color);
    }
}

@keyframes words {
    0%, 20% {
        content: 'Programmer';
    }
    21%, 40% {
        content: 'Youtuber';
    }
    41%, 60% {
        content: 'Designer';
    }
    61%, 80% {
        content: 'Computer expert';
    }
    81%, 100% {
        content: 'Content creater and editor';
    }
}

@keyframes typing {
    0% {
        width: 0;
    }
    5%, 20%, 25%, 40%, 45%, 60%, 65%, 80%, 85% {
        width: calc(100% + 8px);
    }
    10%, 15%, 30%, 35%, 50%, 55%, 70%, 75%, 90%, 95% {
        width: 0;
    }
}


@media  (max-width:1000px) {
    .home {
        gap: 4rem;
    }
}
    
@media (max-width:995px) {
    .home {
        flex-direction: column;
        margin: 5rem 4rem;
    }
    .home .home-content h3 {
        font-size: 2.5rem;
    }
    .home-content h1 {
        font-size: 5rem;
    }
    .home-img img {
        width: 70vw;
        margin-top: 4rem;
    }
}

.services {
    background: var(--second-bg-color);

}
.services-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    align-items: center;
    gap: 2.5rem;
}
.services-box {
    background-color: var(--main-color);
    height: 300px;
    border-radius: 3rem;
    cursor: pointer;
    transition: 0.3s ease;
}

.services-box:hover {
    background: white;
    color: var(--main-color);
    transform: scale(1.03);
    border: 1px solid var(--main-color);
}

.services-box .services-info {   
    display: flex;
    flex-direction: column;
    text-align: left;
    max-height: 200px;
    justify-content: center;
    align-items: baseline;
    padding: 5em;
}

.services-info h4 {
    font-size: 2.5rem;
    font-weight: 500;
    margin-bottom: 1rem;
}

.services-info p {
    font-size: 1.6rem;
    font-weight: 400;
    max-height: 100px;
    margin: auto;
}

@media (max-width:991px) {
    section {
        padding: 10rem 3% 2rem;
    }
    .services{
        padding-bottom: 7rem;
    }
}

@media (max-width:895px){
    .services h2{
        margin-bottom: 3rem;
    }
    .services-container {
        grid-template-columns: repeat(1,1fr);
    }
}

/* Corrected CSS */
.skills {
    background: var(--second-bg-color);
}

/* ... (rest of your CSS remains the same) */

.skills .container {
    background: #e1352c54;
    color: var(--text-color);
    border-radius: 1rem;
    padding: 2rem;
    width: 70%;
    margin: auto;
    margin-top: 2rem;
}
.skills .container .row {
    display: grid;
    grid-template-columns: repeat(5,1fr);
    flex-wrap: wrap;
    gap:1.8rem;
}

.skills .container .bar {
    margin-bottom: 15px;
    padding: 10px;
    border-radius: 1rem;
    background: #e13c26;
    box-shadow: 0 4px 10px var(--main-color);
    transition: 0.3s ease;
    
}

.skills .container .bar .info img {
    width: 50px; /* Set your preferred width */
    height: 50px; /* Set your preferred height */
}
.skills .container .bar:hover {
    box-shadow: 0 4px 10px var(--main-color);
    transform: scale(1.03);

}
.skills .container .bar .info {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1rem;
    margin-top: 1rem;
    
}

.skills .container .bar .info span{
    font-size: 2rem;
    font-weight: 500;
    margin-left: 0.5rem;
    
}

.education {
    background: var(--second-bg-color);

}
.education .timeline {
    position: relative;
    max-width: 1200px;
    margin: 0 auto;
}

.education .timeline::after {
    content: '';
    position: absolute;
    width: 6px;
    background: rgb(90, 64, 64);
    top: 0;
    bottom: 0;
    left: 50%;
    margin-left: -3px;
    z-index:-2;

}

.education .container {
    content: '\f501';
    position: absolute;
    width: 25px;
    height: 25px;
    line-height: 25px;
    right: -17px;
    background-color: rgb(252, 252, 252);
    border: 4px solid var(--main-color);
    top: 15px;
    border-radius: 50%;
    z-index: 100;
}

.education .container::after{
    content: '\f501';
    position: absolute;
    width: 25px;
    height: 25px;
    line-height: 25px;
    right: -17px;
    background-color: rgb(252, 252, 252);
    border: 4px solid var(--main-color);
    top: 15px;
    border-radius: 50%;
    z-index: 100;
    font-size: 1.5rem;
    text-align: center;
    font-weight: 600;
    font-family: "Font Awesome\ 5 Free";
}


.education .left {
    left: 0;
}
.education .right {
    left: 50%;
}

.education .left::before {
    content: '';
    height: 0;
    position: absolute;
    top: 22px;
    width: 0;
    z-index: 1;
    right: 30px;
    border: medium solid var(--main-color);
    border-width: 10px 0 10px 10px;
}

.education .right::before {
    content: '';
    height: 0;
    position: absolute;
    top: 22px;
    width: 0;
    z-index: 1;
    right: 30px;
    border: medium solid var(--main-color);
    border-width: 10px 0 10px 10px;
    border-color: transparent var(--main-color) transparent transparent;
}


.education .right::after{
    left: -16px;
}

.education .content {
    background: var(--main-color);
    position: relative;
    border-radius: 6px;
}
.education .content .tag {
    font-size: 1.5rem;
    padding-top: 1.5rem;
    padding-left: 1.5rem;
}

.education .content .decs {
    margin-left: 1.5rem;
    padding-bottom: 1rem;
}

.education .content .decs h3 {
    font-size: 1.5rem;
    font-weight: 600;
}


.education .content .decs p {
    font-size: 1.3rem;
    font-weight: 500;
    color: #000;
}
@media  screen and (max-width:600px) {
    .education .timeline {
        margin-top: 2rem;
    }
    .education .timeline::after {
        left: 31px;
    }
    .education .container {
        width: 100%;
        padding-left: 8rem;
        padding-right: 2rem;
    }
    
    .education  .container::before {
        left:   61px;
        border: medium solid var(--main-color);
        border-width: 10px 10px 10px 0;
        border-color: transparent var(--main-color) transparent transparent;
    }
    .education .left::after {
        left: 15px;
    }
    .education .right {
        left: 0px;

    }
}


.contact h2 {
    margin-bottom: 3rem;
    color: #fff;
}
.contact form {
    max-width: 70rem;
    margin: 1rem auto;
    margin-bottom: 3rem;
    text-align: center;
}

.contact form .input-box input,
.contact form textarea {
    width: 100%;
    padding: 1rem;
    font-size: 1.6rem;
    color: var(--text-color);
    background: var(--bg-color);
    border-radius: 0.8rem;
    border: 2px solid var(--main-color);
    margin: 1rem 0;
    resize: none;
}

.contact form .btn {
    margin-top: 2rem;
}



.footer {
    position: relative;
    bottom: 0;
    width: 100%;
    padding: 40px 0;
    background-color: var(--main-color);

}
.footer .social {
    text-align: center;
    padding-bottom: 25px;
    color:#000;

}

.footer.social a {
    font-size: 25px;
    color: black;
    border: 2px solid black;
    width: 42px;
    height: 42px;
    display: inline-block;
    text-align: center;
    border-radius: 50%;
    margin: 0 10px;
    transition: 0.3s ease;
}

.footer .social a:hover {
    transform: scale(1.2)translateY(-5px);
    background: black;
    color: var(--main-color);
}

.footer ul {
    margin-top: 0;
    padding: 0;
    font-size: 18px;
    line-height: 1.8;
    margin-bottom: 0;
    text-align: center;
}

.footer ul li a {
    color: #000;
    border-bottom: 3px solid transparent;
    transition: 0.3s ease;
}


.footer ul li a:hover {
    border-bottom: 3px solid black;
}

.footer ul li {
    display: inline-block;
    padding: 0 15px;
}

.footer .copyright {
    margin-top: 50px;
    text-align: center;
    font-size: 16px;
    color: black;

}


@media (max-width:1285px) {
    html {
        font-size: 55%;
    }
    .services-container {
        padding-bottom: 7rem;
        grid-template-columns: repeat(2, 1fr);
        margin: 0 5rem;
    }
}
@media (max-width:991px){
    .header {
        padding: 2rem 3%;
    }
    section {
        padding: 10rem 3% 2rem;
    }
    .services {
        padding-bottom: 7rem;
    }
    .footer {
        padding: 2rem 3%;
    }
    
}