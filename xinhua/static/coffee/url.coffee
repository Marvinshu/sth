$('button[type="button"]').click ->
    cata = $('select[name="cata"]').val()
    source = $('select[name="source"]').val()
    url = $('textarea[name="url"]').val()

    data = {
        cata: cata,
        source: source,
        url: url
    }

    $.only_ajax({
        url: "/j/url",
        data: data
        success: (r)->
            if r.result
                $('input[name="url"]').val('')
                $.tip("添加成功！<br>#{url}")
            else
                $.alert(r.msg)
    })
