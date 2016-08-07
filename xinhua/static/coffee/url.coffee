$('button[type="button"]').click ->
    cata = $('select[name="cata"]').val()
    source = $('select[name="source"]').val()
    url = $('input[name="url"]').val()

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
                $('select[name="cata"] option:first').attr('selected',true)
                $('select[name="source"] option:first').attr('selected',true)
                $('input[name="url"]').val('')
                $.tip("添加成功！<br>#{url}")
            else
                $.alert(r.msg)
    })
