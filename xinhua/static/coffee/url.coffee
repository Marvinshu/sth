$('button[type="button"]').click ->
    cata = $('select[name="cata"]').val()
    source = $('select[name="source"]').val()
    url = $('input[name="url"]').val()
    title= $('input[name="title"]').val()

    data = {
        cata: cata,
        source: source,
        url: url,
        title: title
    }

    $.only_ajax({
        url: "/j/url",
        data: data
        success: (r)->
            if r.result
                $('select[name="cata"] option:first').attr('selected',true)
                $('select[name="source"] option:first').attr('selected',true)
                $('input[name="url"]').val('')
                $('input[name="title"]').val('')
                $.tip("添加成功！<br>#{url}")
            else
                $.alert(r.msg)
    })
