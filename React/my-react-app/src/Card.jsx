import profilePic from "./assets/ansh.jpg"

function Card(){

    return(
        <div className='card'>
            <img className="card-img" src={profilePic} alt="This is me" width={250} height={250}/>
            <h2 className="card-title">Ansh Kumar</h2>
            <p className="card-text">I am Ansh Kumar And I currently learning React</p>
        </div>
    );
}

export default Card