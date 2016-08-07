$('.btn-del').click ->
    self = $(this)
    bootbox.confirm("确定删除？", (result)->
        if result
            id = self.attr('data-id')
            $.only_ajax({
                url: "/j/url/rm",
                data: {id: id}
                success: (r)->
                    window.location.reload()
            })
    )
