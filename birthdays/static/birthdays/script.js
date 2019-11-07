$(document).ready(function () {

    $('#seeAll').click(() => {
        $.ajax({
            url: '/all/',
            success: (data) => {
                var htmlData = ``;
                for (var i in data) {
                    htmlData += `
                    <a href="birthdays/${ data[i].id }/">
                        <div class="row person-row">
                            <div class="col-1 pic-col">
                                <img class="person-pic" alt="person-picture" src="${ data[i].picture }" />
                            </div>
                            <div class="col-10 col-10">
                                <p class="person-name">${ data[i].name }</p>
                            </div>
                         </div>
                    </a>`;
                }
                $('#today-list').html(htmlData)
                document.getElementById('seeAll').style.visibility = "hidden";
                document.getElementById('seeAll').style.display = "none";
                document.getElementById('seeToday').style.visibility = "visible";
                document.getElementById('seeToday').style.display = "inline";
                document.getElementById('subAll').style.visibility = "hidden";
                document.getElementById('subAll').style.display = "none";
                document.getElementById('subToday').style.visibility = "visible";
                document.getElementById('subToday').style.display = "inline";
            }
        });
    });

    $('#submit').click(() => {
        var data={};
        data['name'] = document.getElementById('name').value;
        data['birthday'] = document.getElementById('birthday').value;
        data['picture'] = document.getElementById('picture').value;
        data['fun_fact'] = document.getElementById('fun_fact').value;
        data['present-what'] = document.getElementById('present-what').value;
        data['present-price'] = document.getElementById('present-price').value;
        $.ajax({
            url: '/new/',
            type: 'POST',
            data: data,
            success: (result) => {
                if(result['id']==undefined){
                    alert(result['error'])
                }else{
                    window.location.href = `/birthdays/${result['id']}`;
                }
            }
        });
    });

    $('#add-present').click(() => {
        document.getElementById('present-container').style.visibility = "visible";
        document.getElementById('present-container').style.display = "block";
    });

    $('#present-cancel').click(() => {
        document.getElementById('present-container').style.visibility = "hidden";
        document.getElementById('present-container').style.display = "none";
    });

    $('#present-submit').click(() => {
        var data ={};
        data['present-what'] = document.getElementById('present-w').value;
        data['present-price'] = document.getElementById('present-p').value;
        var person_id = document.getElementById('person-id').innerHTML;
        $.ajax({
            url: `/birthdays/${person_id}/`,
            type: 'PUT',
            data: data,
            success: (result) => {
                if(result['data']=="OK"){
                    document.getElementById('present-container').style.visibility = "hidden";
                    document.getElementById('present-container').style.display = "none";
                    var present_text = document.getElementById('present-text');
                    present_text.innerHTML = `${data['present-what']}, £${data['present-price']}`;
                }else{
                    alert(result['data']);
                }
            }
        });
    });

    $('#delete-person').click(() => {
        var person_id = document.getElementById('person-id').innerHTML;
        var person_name = document.getElementById('person-name').innerHTML;
        if(confirm(`Are you sure you want to delete ${person_name}?`)){
            $.ajax({
                url: `/birthdays/${person_id}/`,
                type: 'DELETE',
                success: (result) => {
                    if(result['data']=="OK"){
                        window.location.href = "/";
                    }else{
                        alert(result['data']);
                    }
                }
            });
        }
    });

    $('#seeToday').click(() => {
        location.reload();
    });

    goBack = () => {
        window.history.back();
    }

});